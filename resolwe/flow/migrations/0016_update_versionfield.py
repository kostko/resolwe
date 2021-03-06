# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-01-24 05:07
from __future__ import unicode_literals

from django.db import migrations
import versionfield


class Migration(migrations.Migration):

    dependencies = [
        ('flow', '0015_make_data_indexes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='version',
            field=versionfield.VersionField(default='0.0.0'),
        ),
        migrations.AlterField(
            model_name='data',
            name='version',
            field=versionfield.VersionField(default='0.0.0'),
        ),
        migrations.AlterField(
            model_name='descriptorschema',
            name='version',
            field=versionfield.VersionField(default='0.0.0'),
        ),
        migrations.AlterField(
            model_name='entity',
            name='version',
            field=versionfield.VersionField(default='0.0.0'),
        ),
        migrations.AlterField(
            model_name='process',
            name='version',
            field=versionfield.VersionField(default='0.0.0'),
        ),
        migrations.AlterField(
            model_name='storage',
            name='version',
            field=versionfield.VersionField(default='0.0.0'),
        ),
        migrations.AlterField(
            model_name='trigger',
            name='version',
            field=versionfield.VersionField(default='0.0.0'),
        ),
    ]
