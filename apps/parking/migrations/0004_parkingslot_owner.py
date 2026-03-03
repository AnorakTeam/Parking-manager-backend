# Add owner FK for OCCUPIED/EXPIRED slots; FREE slots have owner=null

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("parking", "0003_add_start_finish_dates"),
    ]

    operations = [
        migrations.AddField(
            model_name="parkingslot",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="parking_slots",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
