from django.contrib import admin
from apps.parking.models import ParkingSlot


@admin.register(ParkingSlot)
class ParkingSlotAdmin(admin.ModelAdmin):
    list_display = ("id", "line", "position", "status", "vehicle_model", "start_date", "finish_date")
    list_filter = ("line", "status")
    ordering = ("line", "position")
