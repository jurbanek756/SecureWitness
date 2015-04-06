# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('SecureWitness', '0014_report_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='groups',
            field=models.ForeignKey(default=0, to='auth.Group'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='group',
            field=models.ForeignKey(default=0, to='auth.Group'),
            preserve_default=False,
        ),
    ]
