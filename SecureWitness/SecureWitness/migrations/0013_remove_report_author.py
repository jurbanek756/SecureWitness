# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SecureWitness', '0012_customuser_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='author',
        ),
    ]
