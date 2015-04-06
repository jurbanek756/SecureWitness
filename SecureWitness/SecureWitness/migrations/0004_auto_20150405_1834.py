# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0003_auto_20150405_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='author',
            field=models.OneToOneField(to='SecureWitness.CustomUser'),
            preserve_default=True,
        ),
    ]
