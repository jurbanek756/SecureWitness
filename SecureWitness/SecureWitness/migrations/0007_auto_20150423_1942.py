# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0006_report_keyword_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='report_text_long',
            field=models.CharField(max_length=200, unique=True),
            preserve_default=True,
        ),
    ]
