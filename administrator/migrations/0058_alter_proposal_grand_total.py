# Generated by Django 4.1.1 on 2023-02-18 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("administrator", "0057_proposal_grand_total"),
    ]

    operations = [
        migrations.AlterField(
            model_name="proposal",
            name="Grand_Total",
            field=models.FloatField(null=True),
        ),
    ]