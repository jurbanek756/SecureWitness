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
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(verbose_name='last login', default=django.utils.timezone.now)),
                ('admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('reporter', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=20, unique=True)),
                ('email', models.CharField(max_length=50, default='none')),
                ('groups', models.ManyToManyField(to='auth.Group', null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('groups', models.ForeignKey(to='auth.Group', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('report_title', models.CharField(max_length=50)),
                ('report_text_short', models.CharField(max_length=150)),
                ('pub_date', models.DateField(verbose_name='Date Pulished (YYYY-MM-DD)')),
                ('report_text_long', models.CharField(max_length=200, unique=True)),
                ('location', models.CharField(max_length=100)),
                ('file_upload_1', models.FileField(upload_to='', null=True, blank=True)),
                ('file_upload_2', models.FileField(upload_to='', null=True, blank=True)),
                ('file_upload_3', models.FileField(upload_to='', null=True, blank=True)),
                ('file_upload_4', models.FileField(upload_to='', null=True, blank=True)),
                ('incident_date', models.DateField(verbose_name='Incident Date (YYYY-MM-DD)')),
                ('keyword_list', models.CharField(max_length=50, null=True)),
                ('private', models.BooleanField(default=False)),
                ('key', models.CharField(max_length=32, null=True, blank=True)),
                ('author', models.CharField(max_length=50)),
                ('group', models.ForeignKey(to='auth.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='folder',
            name='reports',
            field=models.ForeignKey(to='SecureWitness.Report', blank=True),
            preserve_default=True,
        ),
    ]
