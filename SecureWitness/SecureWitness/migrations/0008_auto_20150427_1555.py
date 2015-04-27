# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0007_auto_20150423_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='file_upload',
            field=models.FileField(null=True, blank=True, upload_to=''),
            preserve_default=True,
        ),
    ]
