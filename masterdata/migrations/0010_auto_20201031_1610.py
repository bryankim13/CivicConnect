# Generated by Django 3.1.1 on 2020-10-31 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('masterdata', '0009_auto_20201031_1425'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issue',
            old_name='emailtemplate',
            new_name='emailtemplates',
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('emailtemplates', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='masterdata.emailtemplate')),
                ('issues', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='masterdata.issue')),
                ('representatives', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='masterdata.representative')),
            ],
        ),
    ]
