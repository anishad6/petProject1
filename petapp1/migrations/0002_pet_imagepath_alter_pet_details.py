# Generated by Django 5.1.1 on 2024-10-09 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petapp1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='imagepath',
            field=models.ImageField(default='', upload_to='image'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='details',
            field=models.CharField(max_length=100),
        ),
    ]
