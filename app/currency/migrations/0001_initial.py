# Generated by Django 4.2.7 on 2024-01-24 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_from', models.EmailField(max_length=255)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='RequestResponseLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255)),
                ('request_method', models.CharField(max_length=10)),
                ('time', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Source')),
                ('logo_source', models.FileField(blank=True, default=None, null=True, upload_to='logo/', verbose_name='logo')),
                ('code_name', models.CharField(max_length=64, unique=True, verbose_name='Code name')),
            ],
            options={
                'verbose_name': 'Source',
                'verbose_name_plural': 'Sources',
            },
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buy', models.DecimalField(decimal_places=2, max_digits=6)),
                ('sell', models.DecimalField(decimal_places=2, max_digits=6)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('currency_type', models.SmallIntegerField(choices=[(2, 'Dollar'), (1, 'Euro')], default=2)),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rates', to='currency.source')),
            ],
            options={
                'verbose_name': 'Rate',
                'verbose_name_plural': 'Rates',
            },
        ),
    ]
