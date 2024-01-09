# Generated by Django 4.1.7 on 2024-01-09 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_remove_hotel_additional_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='hotelname',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Otel adı'),
        ),
        migrations.AlterField(
            model_name='additionalimage',
            name='hotels',
            field=models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, to='myApp.hotel', verbose_name='oteller'),
        ),
        migrations.AlterField(
            model_name='additionalimage',
            name='image',
            field=models.ImageField(max_length=50, upload_to='additional_images'),
        ),
    ]
