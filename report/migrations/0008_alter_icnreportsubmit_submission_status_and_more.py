# Generated by Django 4.2.10 on 2024-04-11 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_admin', '0004_submission_status'),
        ('report', '0007_activityreport_cs_currency_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='icnreportsubmit',
            name='submission_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_admin.submission_status'),
        ),
        migrations.AlterField(
            model_name='icnreportsubmitapproval_f',
            name='approval_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_admin.approvalt_status'),
        ),
        migrations.AlterField(
            model_name='icnreportsubmitapproval_p',
            name='approval_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_admin.approvalf_status'),
        ),
        migrations.AlterField(
            model_name='icnreportsubmitapproval_t',
            name='approval_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_admin.approvalt_status'),
        ),
    ]
