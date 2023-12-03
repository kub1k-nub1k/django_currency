# Generated by Django 4.2.7 on 2023-12-03 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0006_alter_rate_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='currency_type',
            field=models.SmallIntegerField(choices=[(2, 'Dollar'), (1, 'Euro')], default=2),
        ),
    ]
