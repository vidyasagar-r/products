# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20150731_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 31, 11, 11, 55, 875740), blank=True),
        ),
    ]
