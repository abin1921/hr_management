# Generated by Django 5.1.4 on 2024-12-18 10:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_remove_projects_department_id_projects_emp_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='position_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app.position'),
        ),
    ]
