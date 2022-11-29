# Generated by Django 4.1.3 on 2022-11-29 19:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_user_groups_user_user_permissions"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="date_joined",
            field=models.DateTimeField(
                auto_now_add=True,
                default=datetime.datetime(
                    2022, 11, 29, 19, 5, 25, 179471, tzinfo=datetime.timezone.utc
                ),
                verbose_name="date join",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="user",
            name="last_login",
            field=models.DateTimeField(
                auto_now=True,
                default=datetime.datetime(
                    2022, 11, 29, 19, 5, 33, 19015, tzinfo=datetime.timezone.utc
                ),
                verbose_name="last login",
            ),
            preserve_default=False,
        ),
    ]
