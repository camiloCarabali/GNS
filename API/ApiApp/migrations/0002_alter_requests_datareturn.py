# Generated by Django 4.2.4 on 2023-08-04 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requests',
            name='dataReturn',
            field=models.CharField(max_length=10000),
        ),
    ]