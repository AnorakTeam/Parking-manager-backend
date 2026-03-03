from rest_framework import generics
from rest_framework import status as http_status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from apps.parking.models import ParkingSlot
from apps.parking.serializers import (
    ParkingSlotSerializer,
    ParkingSlotStatusUpdateSerializer,
    ParkingSlotOccupySerializer,
)


class ParkingSlotListView(generics.ListAPIView):
    """List all parking slots. Optional query: ?line=1|2|3 to filter by line."""
    serializer_class = ParkingSlotSerializer

    def get_queryset(self):
        qs = ParkingSlot.objects.all()
        line = self.request.query_params.get("line")
        if line is not None:
            try:
                line_num = int(line)
                if 1 <= line_num <= 3:
                    qs = qs.filter(line=line_num)
            except ValueError:
                pass
        return qs


class ParkingSlotDetailView(generics.RetrieveAPIView):
    """Show all information for a particular slot."""
    queryset = ParkingSlot.objects.all()
    serializer_class = ParkingSlotSerializer


class ParkingSlotFreeView(APIView):
    """Free the slot: set status to FREE and clear vehicle_model, start_date, finish_date, owner. Requires auth."""

    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        slot = get_object_or_404(ParkingSlot, pk=pk)
        slot.status = ParkingSlot.Status.FREE
        slot.vehicle_model = ""
        slot.start_date = None
        slot.finish_date = None
        slot.owner = None
        slot.save(update_fields=["status", "vehicle_model", "start_date", "finish_date", "owner"])
        return Response(
            ParkingSlotSerializer(slot).data,
            status=http_status.HTTP_200_OK,
        )


class ParkingSlotOccupyView(APIView):
    """Occupy the slot: set status to OCCUPIED, store vehicle_model, set owner to current user. Slot must be FREE."""

    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        slot = get_object_or_404(ParkingSlot, pk=pk)
        if slot.status != ParkingSlot.Status.FREE:
            return Response(
                {"detail": "Slot is not free. Only FREE slots can be occupied."},
                status=http_status.HTTP_409_CONFLICT,
            )
        serializer = ParkingSlotOccupySerializer(
            slot,
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user)
        return Response(
            ParkingSlotSerializer(slot).data,
            status=http_status.HTTP_200_OK,
        )


class ParkingSlotStatusUpdateView(APIView):
    def patch(self, request, pk):
        slot = get_object_or_404(ParkingSlot, pk=pk)
        serializer = ParkingSlotStatusUpdateSerializer(
            slot,
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            ParkingSlotSerializer(slot).data,
            status=http_status.HTTP_200_OK,
        )
