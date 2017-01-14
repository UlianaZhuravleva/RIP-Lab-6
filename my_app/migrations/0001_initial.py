# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-30 10:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroupModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=20, unique=True)),
                ('base_date', models.DateField()),
                ('genre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MemberModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=20)),
                ('member_surname', models.CharField(max_length=20)),
                ('member_thirdname', models.CharField(max_length=20)),
                ('member_bdate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='MembershipModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('membership_num', models.IntegerField(unique=True)),
                ('join_date', models.DateField()),
                ('out_date', models.DateField()),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='my_app.GroupModel')),
            ],
        ),
        migrations.AddField(
            model_name='membermodel',
            name='membership_num',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='my_app.MembershipModel'),
        ),
    ]
