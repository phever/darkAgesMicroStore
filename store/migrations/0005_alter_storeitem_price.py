# Generated by Django 5.0.7 on 2024-07-17 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_storeitem_visible'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storeitem',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]