# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('report_title', models.CharField(max_length=50)),
                ('report_text_short', models.CharField(max_length=150)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('report_text_long', models.TextField()),
                ('location', models.CharField(max_length=100)),
                ('incident_date', models.DateTimeField()),
                ('keyword_list', models.CharField(max_length=100, default='')),
                ('private', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(verbose_name='last login', default=django.utils.timezone.now)),
                ('admin', models.BooleanField(default=False)),
                ('reporter', models.BooleanField(default=False)),
                ('username', models.CharField(max_length=20, unique=True)),
                ('email', models.CharField(max_length=50, default='none')),
                ('groups', models.ForeignKey(to='auth.Group')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='report',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='report',
            name='group',
            field=models.ForeignKey(to='auth.Group'),
            preserve_default=True,
        ),
    ]
