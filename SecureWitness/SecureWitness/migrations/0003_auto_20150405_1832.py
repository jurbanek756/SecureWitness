# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0002_auto_20150405_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='email',
            field=models.CharField(default='none@none.no', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='report',
            name='author',
            field=models.OneToOneField(to='SecureWitness.CustomUser', default='admin'),
            preserve_default=True,
        ),
    ]
