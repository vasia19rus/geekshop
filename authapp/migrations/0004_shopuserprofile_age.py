# Generated by Django 3.2 on 2021-06-25 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_shopuserprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopuserprofile',
            name='age',
            field=models.CharField(blank=True, max_length=3, verbose_name='возраст'),
        ),
    ]
