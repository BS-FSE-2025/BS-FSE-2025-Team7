# Generated by Django 5.1.4 on 2025-01-02 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_report_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='engineer',
        ),
    ]
