# Generated by Django 5.1.4 on 2024-12-18 10:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_alter_position_department_id_alter_projects_emp_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='position_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.position'),
        ),
    ]
