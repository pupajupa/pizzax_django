# Generated by Django 5.0.1 on 2024-02-05 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
