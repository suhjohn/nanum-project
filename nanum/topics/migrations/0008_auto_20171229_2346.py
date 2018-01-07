# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-29 14:46
from __future__ import unicode_literals

from django.db import migrations
import topics.utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0007_auto_20171209_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='image',
            field=topics.utils.fields.DefaultStaticImageField(blank=True, null=True, upload_to='topic'),
        ),
    ]