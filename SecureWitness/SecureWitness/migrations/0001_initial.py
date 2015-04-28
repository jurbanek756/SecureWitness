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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('reporter', models.BooleanField(default=False)),
                ('name', models.CharField(unique=True, max_length=20)),
                ('email', models.CharField(default='none', max_length=50)),
                ('groups', models.ManyToManyField(null=True, to='auth.Group')),
                ('user', models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('groups', models.ForeignKey(blank=True, to='auth.Group')),
                ('owner', models.OneToOneField(default=None, to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_title', models.CharField(max_length=50)),
                ('report_text_short', models.CharField(max_length=150)),
                ('pub_date', models.DateField(verbose_name='Date Pulished (YYYY-MM-DD)')),
                ('report_text_long', models.CharField(unique=True, max_length=200)),
                ('location', models.CharField(max_length=100)),
                ('file_upload_1', models.FileField(blank=True, null=True, upload_to='')),
                ('file_upload_2', models.FileField(blank=True, null=True, upload_to='')),
                ('file_upload_3', models.FileField(blank=True, null=True, upload_to='')),
                ('file_upload_4', models.FileField(blank=True, null=True, upload_to='')),
                ('incident_date', models.DateField(verbose_name='Incident Date (YYYY-MM-DD)')),
                ('keyword_list', models.CharField(max_length=50, null=True)),
                ('private', models.BooleanField(default=False)),
                ('key', models.CharField(blank=True, max_length=32, null=True)),
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
