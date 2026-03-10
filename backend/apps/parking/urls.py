from django.urls import path
from apps.parking.views import (
    ParkingSlotListView,
    ParkingSlotDetailView,
    ParkingSlotFreeView,
    ParkingSlotOccupyView,
    ParkingSlotStatusUpdateView,
)

urlpatterns = [
    path("slots/", ParkingSlotListView.as_view(), name="parking-slot-list"),
    path("slots/<int:pk>/", ParkingSlotDetailView.as_view(), name="parking-slot-detail"),
    path("slots/<int:pk>/free/", ParkingSlotFreeView.as_view(), name="parking-slot-free"),
    path("slots/<int:pk>/occupy/", ParkingSlotOccupyView.as_view(), name="parking-slot-occupy"),
    path(
        "slots/<int:pk>/status/",
        ParkingSlotStatusUpdateView.as_view(),
        name="parking-slot-status-update",
    ),
]
