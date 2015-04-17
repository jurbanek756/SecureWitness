# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('reporter', models.BooleanField(default=False)),
                ('name', models.CharField(unique=True, max_length=20)),
                ('email', models.CharField(default='none', max_length=50)),
                ('groups', models.ManyToManyField(to='auth.Group', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('report_title', models.CharField(max_length=50)),
                ('report_text_short', models.CharField(max_length=150)),
                ('pub_date', models.DateField(verbose_name='Date Pulished (YYYY-DD-MM)')),
                ('report_text_long', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=100)),
                ('incident_date', models.DateField(verbose_name='Incident Date (YYYY-DD-MM)')),
                ('file_upload', models.FileField(upload_to='', null=True)),
                ('keyword_list', models.CharField(null=True, max_length=100)),
                ('private', models.BooleanField(default=False)),
                ('author', models.CharField(max_length=50)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
