# Generated by Django 4.1.7 on 2024-01-10 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0009_hotel_hotellocationmap'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='hotellocation',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Otel adresi'),
        ),
    ]
