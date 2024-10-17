# Generated by Django 5.1.1 on 2024-10-07 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Pet Name')),
                ('type', models.CharField(max_length=20)),
                ('breed', models.CharField(max_length=40)),
                ('gender', models.CharField(max_length=6)),
                ('age', models.IntegerField()),
                ('price', models.IntegerField()),
                ('details', models.CharField(max_length=100, verbose_name='Pet Details')),
            ],
        ),
    ]
