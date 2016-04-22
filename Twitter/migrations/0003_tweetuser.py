# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 09:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Twitter', '0002_auto_20160421_0946'),
    ]

    operations = [
        migrations.CreateModel(
            name='TweetUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('seguidores', models.ManyToManyField(blank=True, related_name='followed_by', to='Twitter.TweetUser')),
            ],
        ),
    ]
