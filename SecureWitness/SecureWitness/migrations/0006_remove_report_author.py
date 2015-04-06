# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0005_auto_20150405_1836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='author',
        ),
    ]
