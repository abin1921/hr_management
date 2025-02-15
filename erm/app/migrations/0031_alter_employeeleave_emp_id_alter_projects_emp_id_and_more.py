# Generated by Django 5.1.4 on 2025-01-09 11:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_employees_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeleave',
            name='emp_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='projects',
            name='emp_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='code',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='customuser',
            name='contact',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='date_hired',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='firstname',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='gender',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='lastname',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='position_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.position'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='salary',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='customuser',
            name='status',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='department_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.department'),
        ),
        migrations.DeleteModel(
            name='Employees',
        ),
    ]
