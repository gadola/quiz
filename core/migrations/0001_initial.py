# Generated by Django 2.2.14 on 2020-11-24 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_name', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='NumberQuizziz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Lesson')),
            ],
        ),
        migrations.CreateModel(
            name='Quizziz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mp3_path', models.FileField(upload_to='mp3/')),
                ('answer', models.CharField(default='', max_length=500)),
                ('number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.NumberQuizziz')),
            ],
        ),
    ]
