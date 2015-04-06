# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0007_remove_customuser_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='email',
            field=models.CharField(default='none@none.no', max_length=50),
            preserve_default=True,
        ),
    ]
