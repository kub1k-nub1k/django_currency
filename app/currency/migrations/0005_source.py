# Generated by Django 4.2.7 on 2023-11-26 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0004_rename_type_rate_currency_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_url', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
    ]
