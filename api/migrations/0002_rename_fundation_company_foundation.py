# Generated by Django 4.1.3 on 2022-11-06 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='fundation',
            new_name='foundation',
        ),
    ]
