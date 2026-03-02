from django.db import models

# Write your models here

class ParkingSlot(models.Model):
    class Status(models.TextChoices):
        FREE = "FREE", "Free"
        OCCUPIED = "OCCUPIED", "Occupied"
        EXPIRED = "EXPIRED", "Expired"

    LINE_CHOICES = [(i, str(i)) for i in range(1, 4)]
    POSITION_CHOICES = [(i, str(i)) for i in range(1, 11)] 

    line = models.PositiveSmallIntegerField(choices=LINE_CHOICES)
    position = models.PositiveSmallIntegerField(choices=POSITION_CHOICES)

    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.FREE,
    )
    vehicle_model = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ["line", "position"]
        constraints = [
            models.UniqueConstraint(
                fields=["line", "position"],
                name="unique_line_position",
            ),
        ]

    def __str__(self):
        return f"Line {self.line} - Slot {self.position}"