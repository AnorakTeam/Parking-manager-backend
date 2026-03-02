from rest_framework import serializers
from apps.parking.models import ParkingSlot


class ParkingSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSlot
        fields = [
            "id",
            "line",
            "position",
            "status",
            "vehicle_model",
        ]
        read_only_fields = ["id", "line", "position"]


class ParkingSlotStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSlot
        fields = ["status", "vehicle_model"]


class ParkingSlotOccupySerializer(serializers.ModelSerializer):
    """For occupy action: require vehicle_model, set status to OCCUPIED."""

    vehicle_model = serializers.CharField(max_length=100, allow_blank=False)

    class Meta:
        model = ParkingSlot
        fields = ["vehicle_model"]

    def update(self, instance, validated_data):
        instance.vehicle_model = validated_data["vehicle_model"]
        instance.status = ParkingSlot.Status.OCCUPIED
        instance.save(update_fields=["vehicle_model", "status"])
        return instance
