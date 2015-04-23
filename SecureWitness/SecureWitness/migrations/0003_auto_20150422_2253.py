# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('SecureWitness', '0002_customuser_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='user',
        ),
        migrations.AddField(
            model_name='report',
            name='group',
            field=models.ForeignKey(to='auth.Group', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='report',
            name='incident_date',
            field=models.DateField(verbose_name='Incident Date (YYYY-MM-DD)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='report',
            name='pub_date',
            field=models.DateField(verbose_name='Date Pulished (YYYY-MM-DD)'),
            preserve_default=True,
        ),
    ]
