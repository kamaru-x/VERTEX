# Generated by Django 4.1.1 on 2023-01-31 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("administrator", "0019_alter_lead_schedule_attachment_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Task",
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
                ("Date", models.DateTimeField()),
                ("Status", models.IntegerField(default=1)),
                ("AddedBy", models.IntegerField(default=0)),
                ("Ip", models.GenericIPAddressField(blank=True, null=True)),
                ("Title", models.CharField(max_length=50)),
                ("Priority", models.CharField(max_length=25)),
                ("Due_Date", models.DateField()),
                ("Descrition", models.TextField()),
                ("Attachment", models.ManyToManyField(to="administrator.attachments")),
                (
                    "Lead",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="administrator.lead",
                    ),
                ),
            ],
        ),
    ]
