# Generated by Django 4.2 on 2023-05-01 09:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_comment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='description',
            field=models.CharField(blank=True, max_length=255, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 1, 12, 25, 4, 229588), verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='date_of_change',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 1, 12, 25, 4, 229588), verbose_name='Дата редактирования'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2023, 5, 1, 12, 25, 4, 233605), verbose_name='Дата добавления'),
        ),
    ]