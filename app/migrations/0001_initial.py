# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-16 05:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('begin_date', models.DateField()),
                ('end_date', models.DateField()),
                ('ended', models.BooleanField(default=False)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('bio', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('primary_language', models.CharField(max_length=20)),
                ('country_code', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('founded_date', models.DateField()),
                ('dissolved_date', models.DateField()),
                ('dissolved', models.BooleanField(default=False)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('release_date', models.DateField()),
                ('release_type', models.CharField(choices=[('AL', 'Album'), ('SI', 'Single'), ('EP', 'EP')], max_length=2)),
                ('language', models.CharField(max_length=20)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Country')),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Label')),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('duration', models.DurationField()),
            ],
        ),
        migrations.AddField(
            model_name='artist',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Country'),
        ),
    ]