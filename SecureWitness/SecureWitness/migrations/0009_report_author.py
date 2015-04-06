# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0008_customuser_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='author',
            field=models.ForeignKey(default=datetime.datetime(2015, 4, 5, 23, 22, 12, 682787, tzinfo=utc), to='SecureWitness.CustomUser'),
            preserve_default=False,
        ),
    ]
