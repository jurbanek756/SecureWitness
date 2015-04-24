# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0004_auto_20150422_2312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='keyword_list',
        ),
    ]
