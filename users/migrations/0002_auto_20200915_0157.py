# Generated by Django 3.1 on 2020-09-15 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, help_text='Please use 100 or less characters', max_length=100, null=True),
        ),
    ]