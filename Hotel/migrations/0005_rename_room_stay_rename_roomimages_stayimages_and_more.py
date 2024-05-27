# Generated by Django 5.0 on 2024-05-18 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel', '0004_city_alter_hotel_city_features'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Room',
            new_name='Stay',
        ),
        migrations.RenameModel(
            old_name='RoomImages',
            new_name='StayImages',
        ),
        migrations.RenameField(
            model_name='hotelreservation',
            old_name='room_id',
            new_name='stay_id',
        ),
        migrations.RenameField(
            model_name='stay',
            old_name='room_type',
            new_name='stay_type',
        ),
        migrations.RenameField(
            model_name='stayimages',
            old_name='room',
            new_name='stay',
        ),
    ]
