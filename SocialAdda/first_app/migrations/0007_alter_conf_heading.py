# Generated by Django 3.2.5 on 2022-02-15 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0006_alter_conf_heading'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conf',
            name='heading',
            field=models.CharField(max_length=300),
        ),
    ]
