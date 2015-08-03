# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(default=datetime.datetime(2015, 7, 31, 11, 7, 50, 452493), blank=True)),
                ('auth_user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='products',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'products/static/products/product_photo', blank=True),
        ),
        migrations.AddField(
            model_name='basket',
            name='product',
            field=models.ForeignKey(to='products.Products'),
        ),
    ]
