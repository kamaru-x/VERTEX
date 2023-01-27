# Generated by Django 4.1.1 on 2023-01-27 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("administrator", "0007_lead_update"),
    ]

    operations = [
        migrations.CreateModel(
            name="Attachments",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Attachment", models.FileField(upload_to="update-files")),
                (
                    "Lead_Update",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="administrator.lead_update",
                    ),
                ),
            ],
        ),
    ]
