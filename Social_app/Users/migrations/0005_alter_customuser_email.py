# Generated by Django 4.2.9 on 2024-08-11 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_customuser_date_of_birth_customuser_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True),
        ),
    ]
