# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0002_customuser_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='user',
        ),
        migrations.AddField(
            model_name='report',
            name='key',
            field=models.CharField(null=True, max_length=50, blank=True),
            preserve_default=True,
        ),
    ]
