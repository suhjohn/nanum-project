# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 09:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0004_auto_20171125_1812'),
        ('users', '0007_auto_20171125_1812'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AnswerComment',
        ),
        migrations.DeleteModel(
            name='NestedComment',
        ),
        migrations.DeleteModel(
            name='QuestionComment',
        ),
        migrations.AddField(
            model_name='posttype',
            name='answer',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.Answer'),
        ),
        migrations.AddField(
            model_name='posttype',
            name='question',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.Question'),
        ),
        migrations.AddField(
            model_name='comment',
            name='parent_comment',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children_comments', to='posts.Comment'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.PostType'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]