# Generated by Django 4.2.10 on 2024-04-07 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0004_activityreport_aworeda'),
    ]

    operations = [
        migrations.AddField(
            model_name='icnreport',
            name='cs_currency',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'USD'), (2, 'ETB')], default=1, null=True),
        ),
        migrations.AddField(
            model_name='icnreport',
            name='mc_currency',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'USD'), (2, 'ETB')], default=1, null=True),
        ),
    ]
