# Generated by Django 2.0 on 2018-01-31 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0036_auto_20180130_1249'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bounty',
            options={'verbose_name_plural': 'Bounties'},
        ),
        migrations.AddField(
            model_name='tip',
            name='from_address',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='tip',
            name='receive_address',
            field=models.CharField(default='', max_length=255),
        ),
    ]