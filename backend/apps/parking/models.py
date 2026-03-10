from django.conf import settings
from django.db import models

# Slots that are OCCUPIED or EXPIRED have start_date/finish_date and owner; FREE slots have these null.
# Owner is not exposed in list/detail API responses.


class ParkingSlot(models.Model):
    class Status(models.TextChoices):
        FREE = "FREE", "Free"
        OCCUPIED = "OCCUPIED", "Occupied"

    LINE_CHOICES = [(i, str(i)) for i in range(1, 4)]
    POSITION_CHOICES = [(i, str(i)) for i in range(1, 11)] 

    line = models.PositiveSmallIntegerField(choices=LINE_CHOICES)
    position = models.PositiveSmallIntegerField(choices=POSITION_CHOICES)

    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.FREE,
    )
    start_date = models.DateTimeField(null=True, blank=True)
    finish_date = models.DateTimeField(null=True, blank=True)
    
    owner_id = models.IntegerField(null=True, blank=True)

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