# Generated by Django 2.1.4 on 2018-12-07 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_order',
            field=models.DateField(auto_now=True),
        ),
    ]