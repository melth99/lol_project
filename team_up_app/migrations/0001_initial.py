# Generated by Django 5.1.7 on 2025-03-13 19:43

from django.db import migrations, models



class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=15)),
                ('top', models.CharField(max_length=15)),
                ('mid', models.CharField(max_length=15)),
                ('bot', models.CharField(max_length=15)),
                ('support', models.CharField(max_length=15)),
                ('jungle', models.CharField(max_length=15)),
            ],
        ),
    ]
