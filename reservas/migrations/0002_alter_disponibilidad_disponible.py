# Generated by Django 5.1.6 on 2025-02-26 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reservas", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="disponibilidad",
            name="disponible",
            field=models.IntegerField(verbose_name="disponible"),
        ),
    ]
