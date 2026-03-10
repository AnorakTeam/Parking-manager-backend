from django.contrib import admin
from apps.parking.models import ParkingSlot


@admin.register(ParkingSlot)
class ParkingSlotAdmin(admin.ModelAdmin):
    list_display = ("id", "line", "position", "status", "owner_id", "start_date", "finish_date")
    list_filter = ("line", "status")
    ordering = ("line", "position")
