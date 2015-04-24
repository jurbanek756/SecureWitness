# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0003_auto_20150419_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='key',
            field=models.CharField(null=True, max_length=16, blank=True),
            preserve_default=True,
        ),
    ]
