# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0009_report_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='author',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
