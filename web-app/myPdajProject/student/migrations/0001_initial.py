# Generated by Django 2.2.16 on 2020-12-05 11:41

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('index_num', models.CharField(max_length=10, unique=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveIntegerField(default=10, validators=[django.core.validators.MinValueValidator(5), django.core.validators.MaxValueValidator(10)])),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='student.Student')),
            ],
        ),
    ]
