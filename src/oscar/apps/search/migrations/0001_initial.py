# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-13 14:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Synonym',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('synonyms', models.CharField(help_text='Comma-separated list of synonyms, optionally mapped using "=>" to what they should be rewritten to.', max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Synonyms',
                'verbose_name': 'Synonym',
                'abstract': False,
            },
        ),
    ]
