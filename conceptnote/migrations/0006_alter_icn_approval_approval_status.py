# Generated by Django 4.2.10 on 2024-03-22 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conceptnote', '0005_rename_cost_sharing_budget_usd_icn_cost_sharing_budget_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='icn_approval',
            name='approval_status',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Pending_Review'), (2, 'Require Update'), (3, 'Approved'), (4, 'Rejected')], default=1, null=True),
        ),
    ]
