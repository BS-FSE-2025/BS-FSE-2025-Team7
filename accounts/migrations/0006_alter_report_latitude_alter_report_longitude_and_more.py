# Generated by Django 5.1.4 on 2025-01-02 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_report_updated_at_alter_report_latitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='reports/photos/'),
        ),
        migrations.AlterField(
            model_name='report',
            name='status',
            field=models.CharField(choices=[('open', 'Open'), ('in_progress', 'In Progress'), ('resolved', 'Resolved')], default='open', max_length=20),
        ),
    ]
