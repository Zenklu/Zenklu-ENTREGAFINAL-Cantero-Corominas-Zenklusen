# Generated by Django 4.0.6 on 2022-09-02 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_artistica_papeleria'),
    ]

    operations = [
        migrations.AddField(
            model_name='libreria',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='articles/'),
        ),
    ]
