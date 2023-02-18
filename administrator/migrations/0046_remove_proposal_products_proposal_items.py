# Generated by Django 4.1.1 on 2023-02-14 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("administrator", "0045_product_description"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="proposal",
            name="Products",
        ),
        migrations.CreateModel(
            name="Proposal_Items",
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
                ("Quantity", models.IntegerField()),
                ("Total", models.FloatField()),
                (
                    "Product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="administrator.product",
                    ),
                ),
                (
                    "Proposal",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="administrator.proposal",
                    ),
                ),
            ],
        ),
    ]