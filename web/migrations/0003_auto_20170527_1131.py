# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-27 03:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20170527_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='author',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='web.UserProfile'),
        ),
    ]
