# Generated by Django 4.2.2 on 2023-07-10 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizApp', '0004_alter_quiz_correct'),
    ]

    operations = [
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=50)),
                ('content', models.TextField(verbose_name='TEXT')),
                ('category', models.CharField(max_length=30, verbose_name='CATEGORY')),
            ],
        ),
    ]
