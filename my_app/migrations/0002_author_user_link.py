# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-11 09:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='user_link',
            field=models.TextField(blank=True, null=True),
        ),
    ]
