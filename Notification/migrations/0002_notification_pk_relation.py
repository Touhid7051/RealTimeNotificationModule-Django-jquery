# Generated by Django 3.0.8 on 2021-01-17 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notification', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='pk_relation',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
