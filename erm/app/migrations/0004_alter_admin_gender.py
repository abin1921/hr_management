# Generated by Django 5.1.4 on 2024-12-16 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_admin_date_added_remove_admin_date_updated_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='gender',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
