# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-08 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0034_auto_20171208_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quilldeltaoperation',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='answer'),
        ),
    ]
