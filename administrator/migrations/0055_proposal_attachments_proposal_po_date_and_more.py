# Generated by Django 4.1.1 on 2023-02-16 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("administrator", "0054_task_salesman"),
    ]

    operations = [
        migrations.AddField(
            model_name="proposal",
            name="Attachments",
            field=models.ManyToManyField(to="administrator.attachments"),
        ),
        migrations.AddField(
            model_name="proposal",
            name="PO_Date",
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name="proposal",
            name="PO_Number",
            field=models.CharField(max_length=50, null=True),
        ),
    ]