# Generated by Django 4.1.5 on 2023-01-08 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whatToDad_app', '0003_activity_activitycomments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitycomments',
            name='content',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
