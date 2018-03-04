# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-27 04:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mentee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_of_interest', models.CharField(choices=[('data science', 'Data Science'), ('backend devops', 'Back End / DevOps'), ('web full stack', 'Web / Full Stack Development'), ('unknown', 'Unknown')], default='unknown', max_length=30)),
                ('goals', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mentor_status', models.CharField(choices=[('approved', 'Approved'), ('pending', 'Pending'), ('unapproved', 'Unapproved')], default='unapproved', max_length=30)),
                ('area_of_expertise', models.CharField(choices=[('data science', 'Data Science'), ('backend devops', 'Back End / DevOps'), ('web full stack', 'Web / Full Stack Development'), ('unknown', 'Unknown')], default='unknown', max_length=30)),
                ('mentee_capacity', models.IntegerField(default=5)),
                ('currently_accepting_mentees', models.BooleanField(default=False)),
            ],
            managers=[
                ('approved_mentors', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slack_handle', models.CharField(blank=True, max_length=40, null=True)),
                ('linked_in_url', models.URLField(blank=True, null=True)),
                ('repo_url', models.URLField(blank=True, null=True)),
                ('bio', models.TextField()),
                ('email_confirmed', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='mentor',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mentorship_profile.Profile'),
        ),
        migrations.AddField(
            model_name='mentee',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mentorship_profile.Profile'),
        ),
    ]
