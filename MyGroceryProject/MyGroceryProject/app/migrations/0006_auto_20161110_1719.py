# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-10 23:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20161110_1717'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advertisement',
            old_name='date_Of_End',
            new_name='date_of_end',
        ),
        migrations.RenameField(
            model_name='advertisement',
            old_name='date_Of_Start',
            new_name='date_of_start',
        ),
        migrations.RenameField(
            model_name='advertisement',
            old_name='premium_User',
            new_name='premium_user',
        ),
        migrations.RenameField(
            model_name='advertisement',
            old_name='time_Of_Post',
            new_name='time_of_post',
        ),
        migrations.RenameField(
            model_name='advertisement_list',
            old_name='premium_User',
            new_name='premium_user',
        ),
        migrations.RenameField(
            model_name='advertisement_list',
            old_name='time_Of_Post',
            new_name='time_of_post',
        ),
        migrations.RenameField(
            model_name='product_list',
            old_name='premium_User',
            new_name='premium_user',
        ),
    ]