# Generated by Django 4.0.4 on 2022-05-03 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quran', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ayeh',
            name='translate',
        ),
    ]
