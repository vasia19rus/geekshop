# Generated by Django 3.2 on 2021-06-23 14:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_auto_20210620_1501'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopUserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagline', models.CharField(blank=True, max_length=128, verbose_name='тэги')),
                ('about_me', models.TextField(blank=True, max_length=512, verbose_name='о себе')),
                ('gender', models.CharField(blank=True, choices=[('M', 'M'), ('W', 'W')], max_length=1, verbose_name='пол')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
