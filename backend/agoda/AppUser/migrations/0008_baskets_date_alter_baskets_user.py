# Generated by Django 4.1.7 on 2024-01-16 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppUser', '0007_baskets_total_price_alter_baskets_hotel'),
    ]

    operations = [
        migrations.AddField(
            model_name='baskets',
            name='date',
            field=models.DateField(blank=True, max_length=11, null=True, verbose_name='Tarih'),
        ),
        migrations.AlterField(
            model_name='baskets',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppUser.userinfo', verbose_name='Kullanıcı'),
        ),
    ]
