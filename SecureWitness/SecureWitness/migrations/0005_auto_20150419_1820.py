# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0004_auto_20150419_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='key',
            field=models.CharField(max_length=32, null=True, blank=True),
            preserve_default=True,
        ),
    ]
