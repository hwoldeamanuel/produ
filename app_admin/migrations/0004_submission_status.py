# Generated by Django 4.2.10 on 2024-04-10 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_admin', '0003_approvalf_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission_Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]
