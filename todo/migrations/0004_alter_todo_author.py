# Generated by Django 4.2.4 on 2023-09-10 21:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0003_remove_todo_file_alter_todo_author_alter_todo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='글쓴이'),
        ),
    ]