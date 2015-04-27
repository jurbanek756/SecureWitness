# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='key',
            field=models.CharField(max_length=32, blank=True, null=True),
            preserve_default=True,
        ),
    ]
