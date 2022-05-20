# Generated by Django 4.0.3 on 2022-05-20 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_patrolanswer_fk_patrol'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patrolanswer',
            name='fk_answer',
        ),
        migrations.AddField(
            model_name='patrolanswer',
            name='answer',
            field=models.CharField(blank=True, help_text='Insert The Possible Answer', max_length=500, null=True, verbose_name='Answer'),
        ),
        migrations.AddField(
            model_name='patrolanswer',
            name='answerBool',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.DeleteModel(
            name='PossibleAnswer',
        ),
    ]
