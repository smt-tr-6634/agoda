# Generated by Django 4.1.7 on 2024-01-16 22:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppUser', '0009_baskets_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baskets',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı'),
        ),
    ]