# Generated by Django 3.1.1 on 2020-10-16 19:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('masterdata', '0003_auto_20201016_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailtemplate',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
