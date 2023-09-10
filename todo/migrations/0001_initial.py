# Generated by Django 4.2.4 on 2023-09-10 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('context', models.TextField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_completed', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='img/')),
                ('file', models.FileField(blank=True, null=True, upload_to='file/')),
            ],
            options={
                'db_table': 'todo_list',
            },
        ),
    ]
