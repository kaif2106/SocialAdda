# Generated by Django 3.2.5 on 2022-02-15 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0005_auto_20220215_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conf',
            name='heading',
            field=models.CharField(default=' ', max_length=200),
        ),
    ]
