# Generated by Django 4.1.1 on 2023-02-24 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("administrator", "0062_receipt_invoice"),
    ]

    operations = [
        migrations.AlterField(
            model_name="invoice",
            name="Date",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="receipt",
            name="Date",
            field=models.DateField(),
        ),
    ]
