# Add start_date and finish_date for OCCUPIED/EXPIRED slots

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("parking", "0002_switch_to_line_position_slots"),
    ]

    operations = [
        migrations.AddField(
            model_name="parkingslot",
            name="start_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="parkingslot",
            name="finish_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
