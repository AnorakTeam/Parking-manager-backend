# Replace ParkingLot + old ParkingSlot with 30 slots in 3 lines (line 1-3, position 1-10)

from django.db import migrations, models


def create_30_slots(apps, schema_editor):
    ParkingSlot = apps.get_model("parking", "ParkingSlot")
    for line in range(1, 4):
        for position in range(1, 11):
            ParkingSlot.objects.create(
                line=line,
                position=position,
                status="FREE",
                vehicle_model="",
            )


def noop_reverse(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("parking", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(name="ParkingSlot"),
        migrations.DeleteModel(name="ParkingLot"),
        migrations.CreateModel(
            name="ParkingSlot",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("line", models.PositiveSmallIntegerField(choices=[(1, "1"), (2, "2"), (3, "3")])),
                ("position", models.PositiveSmallIntegerField(choices=[(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5"), (6, "6"), (7, "7"), (8, "8"), (9, "9"), (10, "10")])),
                (
                    "status",
                    models.CharField(
                        choices=[("FREE", "Free"), ("OCCUPIED", "Occupied"), ("EXPIRED", "Expired")],
                        default="FREE",
                        max_length=10,
                    ),
                ),
                ("vehicle_model", models.CharField(blank=True, max_length=100)),
            ],
            options={
                "ordering": ["line", "position"],
                "constraints": [
                    models.UniqueConstraint(fields=("line", "position"), name="unique_line_position"),
                ],
            },
        ),
        migrations.RunPython(create_30_slots, noop_reverse),
    ]
