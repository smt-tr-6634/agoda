# Generated by Django 4.1.7 on 2024-01-09 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_hotel_hotelname_alter_additionalimage_hotels_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='hotellocation',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Otel Konumu'),
        ),
    ]
