# Generated by Django 4.0.3 on 2022-05-21 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patrolweek',
            name='fk_answers',
            field=models.ManyToManyField(to='home.patrolanswer'),
        ),
    ]
