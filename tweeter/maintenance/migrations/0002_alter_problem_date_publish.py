# Generated by Django 4.1.5 on 2023-02-02 19:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("maintenance", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="problem",
            name="date_publish",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 2, 2, 19, 33, 6, 929320)
            ),
        ),
    ]