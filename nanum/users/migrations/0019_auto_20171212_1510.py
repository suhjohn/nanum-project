# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-12 06:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_auto_20171211_1910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='answer_count',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='upvote_count',
        ),
    ]