# Generated by Django 3.0.5 on 2020-10-24 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signin', '0002_clubs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clubs',
            name='coreteam',
        ),
        migrations.RemoveField(
            model_name='clubs',
            name='members',
        ),
    ]