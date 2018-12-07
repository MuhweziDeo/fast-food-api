# Generated by Django 2.1.4 on 2018-12-07 05:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('location', models.CharField(max_length=100)),
                ('status', models.CharField(default='Pending', max_length=20)),
                ('meal', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.Menu')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]