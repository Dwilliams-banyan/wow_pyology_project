# Generated by Django 4.1.5 on 2023-01-11 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whatToDad_app', '0005_rename_user_id_activity_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='addressStreet',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='activity',
            name='city',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='activity',
            name='state',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='activity',
            name='zip',
            field=models.IntegerField(),
        ),
    ]
