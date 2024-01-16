# Generated by Django 4.1.7 on 2024-01-16 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0024_hotel_discount'),
        ('AppUser', '0006_baskets'),
    ]

    operations = [
        migrations.AddField(
            model_name='baskets',
            name='total_price',
            field=models.IntegerField(blank=True, max_length=11, null=True, verbose_name='Toplam fiyat'),
        ),
        migrations.AlterField(
            model_name='baskets',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.hotel', verbose_name='hotel'),
        ),
    ]
