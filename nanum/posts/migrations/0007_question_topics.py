# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 20:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0004_topic_description'),
        ('posts', '0006_auto_20171126_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='topics',
            field=models.ManyToManyField(related_name='questions', to='topics.Topic'),
        ),
    ]
