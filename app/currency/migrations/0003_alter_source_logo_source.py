# Generated by Django 4.2.7 on 2023-12-26 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0002_source_logo_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='source',
            name='logo_source',
            field=models.FileField(blank=True, default=None, null=True, upload_to='logo/', verbose_name='logo'),
        ),
    ]
