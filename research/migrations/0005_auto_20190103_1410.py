# Generated by Django 2.1.4 on 2019-01-03 14:10

from django.db import migrations, models
import django.db.models.deletion
import research.models


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0004_project_director'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labdirector',
            name='lab',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='research.ResearchLab'),
        ),
        migrations.AlterField(
            model_name='project',
            name='director',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='research.LabDirector'),
        ),
        migrations.AlterField(
            model_name='project',
            name='paper',
            field=models.FileField(upload_to=research.models.user_directory_path),
        ),
    ]
