# Generated by Django 4.0.5 on 2022-06-18 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Neighbourhood', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='hood',
            field=models.CharField(choices=[('Kahawa Sukari', 'Kahawa Sukari'), ('Kahawa West', 'Kahawa West'), ('Kasarani', 'Kasarani')], default=1, max_length=25),
        ),
    ]