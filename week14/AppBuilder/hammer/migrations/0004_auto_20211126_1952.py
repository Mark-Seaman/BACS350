# Generated by Django 3.1.2 on 2021-11-26 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hammer', '0003_auto_20211126_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='expected',
            field=models.TextField(default='Initial Output', null=True),
        ),
    ]
