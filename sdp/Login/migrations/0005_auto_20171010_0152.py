# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 01:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0004_auto_20171010_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
