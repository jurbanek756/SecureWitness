# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('admin', models.BooleanField(default=False)),
                ('reporter', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(default='none', max_length=50)),
                ('groups', models.ManyToManyField(null=True, to='auth.Group')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('report_title', models.CharField(max_length=50)),
                ('report_text_short', models.CharField(max_length=150)),
                ('pub_date', models.DateField(verbose_name='Date Pulished (YYYY-DD-MM)')),
                ('report_text_long', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=100)),
                ('incident_date', models.DateField(verbose_name='Incident Date (YYYY-DD-MM)')),
                ('file_upload', models.FileField(null=True, upload_to='')),
                ('keyword_list', models.CharField(null=True, max_length=100)),
                ('private', models.BooleanField(default=False)),
                ('author', models.CharField(max_length=50)),
                ('group', models.ManyToManyField(null=True, to='auth.Group')),
                ('user', models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
