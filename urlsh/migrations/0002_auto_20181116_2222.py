# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-16 18:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlsh', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='short_link',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]