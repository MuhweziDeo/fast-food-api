# Generated by Django 2.1.4 on 2018-12-07 16:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_order_date_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='meal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meal', to='users.Menu'),
        ),
        migrations.AlterField(
            model_name='order',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
