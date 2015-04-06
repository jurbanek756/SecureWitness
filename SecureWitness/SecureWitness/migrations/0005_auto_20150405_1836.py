# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0004_auto_20150405_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='author',
            field=models.ForeignKey(to='SecureWitness.CustomUser'),
            preserve_default=True,
        ),
    ]
