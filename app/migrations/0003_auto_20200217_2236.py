# Generated by Django 3.0.3 on 2020-02-17 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190829_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tags',
            field=models.ManyToManyField(to='app.Tag'),
        ),
    ]