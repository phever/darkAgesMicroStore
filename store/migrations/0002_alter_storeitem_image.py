# Generated by Django 5.0.7 on 2024-07-16 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storeitem',
            name='image',
            field=models.ImageField(upload_to='static/images/'),
        ),
    ]