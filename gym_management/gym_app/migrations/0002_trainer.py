# Generated by Django 4.2.7 on 2023-11-22 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='trainer',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200, null=True)),
                ('salary', models.IntegerField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
