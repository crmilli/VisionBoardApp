# Generated by Django 5.1.1 on 2024-12-05 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projecta10", "0019_visionboard_websocket_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="caption",
            field=models.CharField(max_length=255),
        ),
    ]
