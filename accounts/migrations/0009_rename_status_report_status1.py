# Generated by Django 5.1.4 on 2025-01-12 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_report_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='status',
            new_name='status1',
        ),
    ]
