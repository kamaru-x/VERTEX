# Generated by Django 4.1.1 on 2023-02-08 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("administrator", "0042_lead_cancel_date_lead_cancel_reason"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lead",
            name="Cancel_Reason",
            field=models.TextField(blank=True, null=True),
        ),
    ]
