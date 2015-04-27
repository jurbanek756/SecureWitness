# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', default=django.utils.timezone.now)),
                ('admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('reporter', models.BooleanField(default=False)),
                ('name', models.CharField(unique=True, max_length=20)),
                ('email', models.CharField(default='none', max_length=50)),
                ('groups', models.ManyToManyField(null=True, to='auth.Group')),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('groups', models.ForeignKey(blank=True, to='auth.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('report_title', models.CharField(max_length=50)),
                ('report_text_short', models.CharField(max_length=150)),
                ('pub_date', models.DateField(verbose_name='Date Pulished (YYYY-MM-DD)')),
                ('report_text_long', models.CharField(unique=True, max_length=200)),
                ('location', models.CharField(max_length=100)),
                ('file_upload_1', models.FileField(null=True, upload_to='', blank=True)),
                ('file_upload_2', models.FileField(null=True, upload_to='', blank=True)),
                ('file_upload_3', models.FileField(null=True, upload_to='', blank=True)),
                ('file_upload_4', models.FileField(null=True, upload_to='', blank=True)),
                ('incident_date', models.DateField(verbose_name='Incident Date (YYYY-MM-DD)')),
                ('keyword_list', models.CharField(null=True, max_length=50)),
                ('private', models.BooleanField(default=False)),
                ('key', models.CharField(null=True, blank=True, max_length=32)),
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
            field=models.ForeignKey(blank=True, to='SecureWitness.Report'),
            preserve_default=True,
        ),
    ]
