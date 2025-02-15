# Generated by Django 5.1.4 on 2024-12-16 12:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_clients'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.TextField()),
                ('owner', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('projects_no', models.IntegerField()),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TrainingType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainer', models.TextField()),
                ('course', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('project_description', models.TextField()),
                ('status', models.IntegerField()),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.clientcompany')),
                ('department_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.department')),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('cost', models.FloatField(default=0)),
                ('status', models.IntegerField()),
                ('training_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.trainingtype')),
            ],
        ),
    ]
