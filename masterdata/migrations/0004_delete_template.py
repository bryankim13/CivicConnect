# Generated by Django 3.1.1 on 2020-11-05 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('masterdata', '0003_remove_emailtemplate_datecreated'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Template',
        ),
    ]
