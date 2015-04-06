# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('admin', models.BooleanField(default=False)),
                ('reporter', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=75)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Custom_User',
        ),
        migrations.AlterField(
            model_name='report',
            name='keywords',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='report',
            name='report_text_long',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
