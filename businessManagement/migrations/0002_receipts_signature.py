# Generated by Django 3.0.7 on 2020-06-29 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('businessManagement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipts',
            name='signature',
            field=models.ImageField(null=True, upload_to='images/signatures'),
        ),
    ]
