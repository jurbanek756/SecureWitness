# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0013_remove_report_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='author',
            field=models.ForeignKey(to='SecureWitness.CustomUser', default=0),
            preserve_default=False,
        ),
    ]
