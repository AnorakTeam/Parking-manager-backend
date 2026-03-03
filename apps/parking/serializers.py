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
            "start_date",
            "finish_date",
        ]
        read_only_fields = ["id", "line", "position"]


class ParkingSlotStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSlot
        fields = ["status", "vehicle_model", "start_date", "finish_date"]


class ParkingSlotOccupySerializer(serializers.ModelSerializer):
    """Occupy slot: vehicle_model required; start_date/finish_date optional. Default finish_date = start_date + 24h."""

    vehicle_model = serializers.CharField(max_length=100, allow_blank=False)
    start_date = serializers.DateTimeField(required=False, allow_null=True)
    finish_date = serializers.DateTimeField(required=False, allow_null=True)

    class Meta:
        model = ParkingSlot
        fields = ["vehicle_model", "start_date", "finish_date"]

    def update(self, instance, validated_data, **kwargs):
        from django.utils import timezone
        from datetime import timedelta

        vehicle_model = validated_data["vehicle_model"]
        start_date = validated_data.get("start_date") or timezone.now()
        finish_date = validated_data.get("finish_date")
        if finish_date is None:
            finish_date = start_date + timedelta(hours=24)
        owner = kwargs.get("owner")

        instance.vehicle_model = vehicle_model
        instance.start_date = start_date
        instance.finish_date = finish_date
        instance.status = ParkingSlot.Status.OCCUPIED
        if owner is not None:
            instance.owner = owner
        instance.save(
            update_fields=["vehicle_model", "start_date", "finish_date", "status", "owner"]
        )
        return instance
