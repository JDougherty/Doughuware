# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('docfile', models.FileField(upload_to=b'documents/%Y/%m/%d')),
                ('thumbnail', models.ImageField(upload_to=b'documents/thumbnails/%Y/%m/%d')),
                ('preview', models.ImageField(upload_to=b'documents/previews/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100, blank=True)),
                ('parent', models.ForeignKey(related_name='children', blank=True, to='core.Tag', null=True)),
            ],
        ),
    ]
