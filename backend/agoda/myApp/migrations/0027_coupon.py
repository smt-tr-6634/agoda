# Generated by Django 5.0.1 on 2024-01-18 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0026_hotel_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titile', models.IntegerField(blank=True, null=True, verbose_name='İndirim Oranı giriniz')),
            ],
        ),
    ]