# Generated by Django 4.1.7 on 2024-01-09 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0004_hotel_hotellocation'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='rating',
            field=models.IntegerField(blank=True, null=True, verbose_name='Değerlendirme Puanı'),
        ),
    ]
