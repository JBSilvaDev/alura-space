# Generated by Django 4.2.7 on 2023-11-12 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("galeria", "0003_fotografia_puplicada"),
    ]

    operations = [
        migrations.RenameField(
            model_name="fotografia",
            old_name="puplicada",
            new_name="publicada",
        ),
    ]
