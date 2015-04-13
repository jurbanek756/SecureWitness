# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('report_title', models.CharField(max_length=50)),
                ('report_text_short', models.CharField(max_length=150)),
                ('pub_date', models.DateField(verbose_name='Date Published (YYYY-DD-MM)')),
                ('report_text_long', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=100)),
                ('incident_date', models.DateField(null=True, verbose_name='Incident Date  (YYYY-DD-MM)')),
                ('file_upload', models.FileField(upload_to='', null=True)),
                ('keyword_list', models.CharField(max_length=100)),
                ('private', models.BooleanField(default=False)),
                ('author', models.CharField(max_length=50)),
                ('group', models.ManyToManyField(null=True, to='auth.Group', related_name='group_login')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
