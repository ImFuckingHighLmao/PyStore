# Generated by Django 4.0.1 on 2022-02-16 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productincart',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
