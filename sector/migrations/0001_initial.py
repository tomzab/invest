# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-02 13:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtailmarkdown.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('wagtailcore', '0040_page_draft_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='SectorLandingPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('heading', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='SectorPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('description', models.TextField()),
                ('heading', models.CharField(max_length=255)),
                ('pullout', wagtail.core.fields.StreamField((('content', wagtail.core.blocks.StructBlock((('text', wagtailmarkdown.blocks.MarkdownBlock()), ('stat', wagtail.core.blocks.CharBlock()), ('stat_text', wagtail.core.blocks.CharBlock())), max_num=1, min_num=1)),))),
                ('subsections', wagtail.core.fields.StreamField((('markdown', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(max_length=255)), ('content', wagtailmarkdown.blocks.MarkdownBlock())))),))),
                ('hero_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
