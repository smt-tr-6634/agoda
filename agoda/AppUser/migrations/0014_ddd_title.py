# Generated by Django 5.0.1 on 2024-01-19 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppUser', '0013_ddd'),
    ]

    operations = [
        migrations.AddField(
            model_name='ddd',
            name='title',
            field=models.TextField(blank=True, max_length=20, null=True, verbose_name='asdasd'),
        ),
    ]