# Generated by Django 3.0.7 on 2020-07-18 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200716_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.CharField(max_length=400000),
        ),
    ]
