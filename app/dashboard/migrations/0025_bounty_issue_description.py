# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-08 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0024_bounty_avatar_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='bounty',
            name='issue_description',
            field=models.TextField(default=''),
        ),
    ]