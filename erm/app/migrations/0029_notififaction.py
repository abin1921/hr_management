# Generated by Django 5.1.4 on 2025-01-02 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_remove_training_cost_training_batch_time_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notififaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('message', models.TextField()),
            ],
        ),
    ]
