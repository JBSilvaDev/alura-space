# Generated by Django 4.2.7 on 2023-11-12 17:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("galeria", "0004_rename_puplicada_fotografia_publicada"),
    ]

    operations = [
        migrations.AddField(
            model_name="fotografia",
            name="data_fotografia",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
