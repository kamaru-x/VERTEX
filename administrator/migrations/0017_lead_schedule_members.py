# Generated by Django 4.1.1 on 2023-01-30 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("administrator", "0016_lead_schedule_schedule_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="lead_schedule",
            name="Members",
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
