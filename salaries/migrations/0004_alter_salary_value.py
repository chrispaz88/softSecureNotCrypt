# Generated by Django 5.0.2 on 2024-03-01 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salaries', '0003_alter_salary_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salary',
            name='value',
            field=models.IntegerField(),
        ),
    ]