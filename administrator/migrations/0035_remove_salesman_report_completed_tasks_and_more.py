# Generated by Django 4.1.1 on 2023-02-03 13:26

import administrator.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("administrator", "0034_attachments_format"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="salesman_report",
            name="Completed_Tasks",
        ),
        migrations.RemoveField(
            model_name="salesman_report",
            name="Pending_Tasks",
        ),
        migrations.AddField(
            model_name="salesman_report",
            name="Leads",
            field=models.ManyToManyField(to="administrator.lead"),
        ),
        migrations.AddField(
            model_name="salesman_report",
            name="Opportunities",
            field=models.IntegerField(
                default=1, verbose_name=administrator.models.Lead
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="salesman_report",
            name="Proposals",
            field=models.IntegerField(
                default=1, verbose_name=administrator.models.Lead
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="salesman_report",
            name="Tasks",
            field=models.ManyToManyField(to="administrator.task"),
        ),
    ]