# Generated by Django 3.0.4 on 2020-03-15 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_auto_20200315_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='produtos'),
        ),
    ]
