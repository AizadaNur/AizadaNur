# Generated by Django 3.0.5 on 2020-04-03 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=300)),
                ('city', models.CharField(max_length=200)),
                ('address', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField(max_length=200)),
                ('salary', models.FloatField()),
                ('comp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Company')),
            ],
        ),
    ]
