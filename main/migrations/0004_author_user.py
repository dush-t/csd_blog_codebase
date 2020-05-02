# Generated by Django 3.0.5 on 2020-04-25 13:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_auto_20200408_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Author', to=settings.AUTH_USER_MODEL),
        ),
    ]