# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-27 20:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urlsh', '0004_auto_20181127_1844'),
    ]

    operations = [
        migrations.RenameField(
            model_name='url',
            old_name='short_link',
            new_name='shortcode',
        ),
    ]
