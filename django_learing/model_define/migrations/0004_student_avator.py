# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-02 08:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_define', '0003_student_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='avator',
            field=models.ImageField(default='imgs/default.png', upload_to='avator/2.png'),
        ),
    ]
