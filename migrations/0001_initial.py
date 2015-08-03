# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('photo', models.ImageField(upload_to='products/product_photo')),
                ('description', models.TextField()),
                ('category', models.ForeignKey(to='products.Category')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('email', models.EmailField(unique=True, max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='user',
            field=models.ForeignKey(to='products.User'),
        ),
        migrations.AddField(
            model_name='category',
            name='user',
            field=models.ManyToManyField(to='products.User'),
        ),
    ]
