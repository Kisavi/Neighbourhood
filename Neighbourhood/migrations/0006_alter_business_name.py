# Generated by Django 4.0.5 on 2022-06-19 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Neighbourhood', '0005_alter_business_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
