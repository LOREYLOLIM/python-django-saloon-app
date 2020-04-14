# Generated by Django 2.1.7 on 2020-04-11 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Phone', models.IntegerField()),
                ('Time', models.DateTimeField(auto_now_add=True)),
                ('Service', models.CharField(max_length=100)),
                ('Description', models.TextField(max_length=500)),
            ],
        ),
    ]