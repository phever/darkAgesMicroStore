# Generated by Django 5.0.7 on 2024-07-17 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_storeitem_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='storeitem',
            name='to_order',
            field=models.BooleanField(default=True),
        ),
    ]