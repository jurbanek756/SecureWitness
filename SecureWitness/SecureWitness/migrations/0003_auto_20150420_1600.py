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
        migrations.AlterField(
            model_name='report',
            name='file_upload',
            field=models.FileField(blank=True, upload_to='', null=True),
            preserve_default=True,
        ),
    ]
