# Generated by Django 4.1.5 on 2023-02-04 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_daily_feed'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='crop_id',
            field=models.IntegerField(default=101),
            preserve_default=False,
        ),
    ]
