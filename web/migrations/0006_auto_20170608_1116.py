# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-08 03:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20170606_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
