# Generated by Django 4.1.1 on 2023-02-16 09:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("administrator", "0053_lead_accepted_proposals_lead_rejected_proposals"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="Salesman",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]