# Generated by Django 4.1.7 on 2024-01-16 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppUser', '0008_baskets_date_alter_baskets_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='baskets',
            name='person',
            field=models.IntegerField(blank=True, max_length=20, null=True, verbose_name='Kişi sayısı'),
        ),
    ]
