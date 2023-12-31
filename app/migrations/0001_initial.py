# Generated by Django 4.2.2 on 2023-07-02 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='pics')),
                ('designation', models.CharField(max_length=150)),
                ('qualification', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=150)),
                ('remarks', models.TextField(default='')),
                ('salary', models.IntegerField()),
                ('Status', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
