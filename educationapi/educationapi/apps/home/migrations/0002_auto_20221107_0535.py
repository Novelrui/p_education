# Generated by Django 2.2.15 on 2022-11-07 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='image_url',
            field=models.ImageField(max_length=255, upload_to='banner', verbose_name='picture'),
        ),
    ]
