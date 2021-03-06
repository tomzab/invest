# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-09 17:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_homepage_subsections'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='how_we_help_lead_in',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='how_we_help_title',
            field=models.CharField(default='How we help', max_length=255),
        ),
        migrations.AddField(
            model_name='homepage',
            name='sector_lead_in',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='sector_title',
            field=models.TextField(default='Set up a business in the UK', max_length=255),
        ),
    ]
