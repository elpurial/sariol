# Generated by Django 5.1.5 on 2025-02-05 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("uno_a_muchos", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="casa_rodolfo",
            old_name="Rodolfo",
            new_name="nombre",
        ),
    ]
