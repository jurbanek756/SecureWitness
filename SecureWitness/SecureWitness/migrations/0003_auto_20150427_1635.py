# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0002_report_key'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='file_upload',
            new_name='file_upload_1',
        ),
        migrations.AddField(
            model_name='report',
            name='file_upload_2',
            field=models.FileField(blank=True, upload_to='', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='report',
            name='file_upload_3',
            field=models.FileField(blank=True, upload_to='', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='report',
            name='file_upload_4',
            field=models.FileField(blank=True, upload_to='', null=True),
            preserve_default=True,
        ),
    ]
