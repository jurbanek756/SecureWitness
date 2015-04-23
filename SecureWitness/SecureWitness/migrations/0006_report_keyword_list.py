# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0005_remove_report_keyword_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='keyword_list',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
    ]
