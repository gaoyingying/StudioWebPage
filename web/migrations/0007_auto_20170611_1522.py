# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-11 07:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20170608_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='subtitle',
            field=models.CharField(default='', max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='page',
            name='subtitle',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]
