# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-05 07:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import model_define.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='文章标题')),
                ('content', models.TextField(verbose_name='文章正文')),
                ('author', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='分类名称')),
                ('desc', models.CharField(default=None, max_length=255, verbose_name='分类描述')),
                ('index', models.IntegerField(default=999, verbose_name='分类的排序')),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
                'db_table': 'category',
                'ordering': ['index', 'id'],
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=10, verbose_name='课程名')),
                ('monitor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='course_monitor_user', to=settings.AUTH_USER_MODEL, verbose_name='课代表')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_teacher_user', to=settings.AUTH_USER_MODEL, verbose_name='任课老师')),
            ],
            options={
                'verbose_name': '课程列表',
                'verbose_name_plural': '课程列表',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(db_index=True, max_length=10, verbose_name='用户名')),
                ('desc', models.TextField(help_text='这里来一些介绍吧，不要超过100个字', max_length=100, verbose_name='个人简介')),
                ('sex', models.IntegerField(choices=[(None, '请选择'), (0, '男'), (1, '女')], verbose_name='性别')),
                ('insert_time', models.DateTimeField(auto_now_add=True, verbose_name='录入时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('english_score', models.FloatField(validators=[model_define.models.check_score], verbose_name='英语成绩')),
                ('schooling', models.DecimalField(decimal_places=2, default=model_define.models.func01, max_digits=7, verbose_name='学费')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('last_login_ip', models.GenericIPAddressField(verbose_name='最后登录IP')),
                ('is_login', models.BooleanField()),
                ('is_login2', models.NullBooleanField()),
                ('avator', models.ImageField(default='avator/default.png', upload_to='avator/', verbose_name='用户头像')),
                ('allow_null', models.CharField(max_length=10, null=True, verbose_name='null=True')),
                ('allow_blank', models.CharField(blank=True, max_length=10, verbose_name='blank=True')),
                ('select', models.CharField(db_column='choices', max_length=10)),
                ('courses', models.ManyToManyField(to='model_define.Course', verbose_name='选修课')),
            ],
            options={
                'verbose_name': '学生表',
                'verbose_name_plural': '学生表',
                'ordering': ['-student_id'],
                'get_latest_by': 'update_time',
            },
        ),
        migrations.AlterUniqueTogether(
            name='article',
            unique_together=set([('title', 'author')]),
        ),
        migrations.AlterIndexTogether(
            name='article',
            index_together=set([('title', 'author')]),
        ),
    ]
