# Generated by Django 4.1.5 on 2023-01-11 00:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whatToDad_app', '0006_alter_activity_addressstreet_alter_activity_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='zip',
            field=models.CharField(max_length=6, validators=[django.core.validators.RegexValidator('^[0-9]{6}$', 'Invalid postal code')]),
        ),
    ]
