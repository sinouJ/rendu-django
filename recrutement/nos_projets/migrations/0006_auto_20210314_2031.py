# Generated by Django 3.1.7 on 2021-03-14 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nos_projets', '0005_auto_20210314_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(upload_to='images'),
        ),
    ]