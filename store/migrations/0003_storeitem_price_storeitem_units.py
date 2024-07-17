# Generated by Django 5.0.7 on 2024-07-17 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_storeitem_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='storeitem',
            name='price',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='storeitem',
            name='units',
            field=models.CharField(choices=[('G', 'Million Gold'), ('C', 'Code(s)')], default='G', max_length=2),
            preserve_default=False,
        ),
    ]