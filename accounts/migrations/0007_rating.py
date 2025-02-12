# Generated by Django 5.1.4 on 2025-01-04 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_report_latitude_alter_report_longitude_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')], verbose_name='Rating')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Comment')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
            ],
            options={
                'verbose_name': 'Rating',
                'verbose_name_plural': 'Ratings',
                'ordering': ['-created_at'],
            },
        ),
    ]
