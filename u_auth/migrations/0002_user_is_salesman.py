# Generated by Django 4.1.1 on 2023-01-27 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("u_auth", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_salesman",
            field=models.BooleanField(default=False),
        ),
    ]
