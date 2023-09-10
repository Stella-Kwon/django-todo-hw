# Generated by Django 4.2.4 on 2023-09-10 20:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='file',
        ),
        migrations.AlterField(
            model_name='todo',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True, verbose_name='글쓴이'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]