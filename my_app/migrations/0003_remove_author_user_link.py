# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-11 09:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_author_user_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='user_link',
        ),
    ]
