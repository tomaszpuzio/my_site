# Generated by Django 3.2.5 on 2021-08-06 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='email_address',
            field=models.EmailField(max_length=50),
        ),
    ]
