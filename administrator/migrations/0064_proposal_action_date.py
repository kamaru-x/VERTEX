# Generated by Django 4.1.1 on 2023-02-25 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("administrator", "0063_alter_invoice_date_alter_receipt_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="proposal",
            name="Action_Date",
            field=models.DateField(null=True),
        ),
    ]