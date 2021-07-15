# Generated by Django 3.2.4 on 2021-07-15 07:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_alter_task_target_batch'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='remainder',
            field=models.CharField(choices=[('None', 'None'), ('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('Week before', 'Week before'), ('Custom', 'Custom')], default='None', max_length=12),
        ),
        migrations.AddField(
            model_name='task',
            name='remainder_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 15, 7, 54, 1, 956256, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='task',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2021, 7, 15, 7, 54, 1, 956256, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 15, 7, 54, 1, 824080, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='target_batch',
            field=models.CharField(choices=[('Self', 'Self'), ('All Batches', 'All Batches'), ('B.Tech', 'B.Tech'), ('B.Tech 20', 'B.Tech 20'), ('B.Tech 19', 'B.Tech 19'), ('B.Tech 18', 'B.Tech 18'), ('B.Tech 17', 'B.Tech 17'), ('B.Tech 16', 'B.Tech 16'), ('B.Des', 'B.Des'), ('B.Des 20', 'B.Des 20'), ('B.Des 19', 'B.Des 19'), ('B.Des 18', 'B.Des 18'), ('B.Des 17', 'B.Des 17'), ('B.Des 16', 'B.Des 16'), ('M.Tech', 'M.Tech'), ('M.Tech 20', 'M.Tech 20'), ('M.Tech 19', 'M.Tech 19'), ('M.Tech 18', 'M.Tech 18'), ('M.Tech 17', 'M.Tech 17'), ('M.Tech 16', 'M.Tech 16'), ('PhD', 'PhD'), ('PhD 20', 'PhD 20'), ('PhD 19', 'PhD 19'), ('PhD 18', 'PhD 18'), ('PhD 17', 'PhD 17'), ('PhD 16', 'PhD 16')], default='Self', max_length=13),
        ),
        migrations.AlterField(
            model_name='task',
            name='target_branch',
            field=models.CharField(choices=[('Self', 'Self'), ('All Branches', 'All Branches'), ('Computer Science and Engineering', 'Computer Science and Engineering'), ('Electronics and Communications Engineering', 'Electronics and Communications Engineering'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Civil Engineering', 'Civil Engineering'), ('Design', 'Design'), ('Biosciences and Bioengineering', 'Biosciences and Bioengineering'), ('Chemical Engineering', 'Chemical Engineering'), ('Electronics and Electrical Engineering', 'Electronics and Electrical Engineering'), ('Engineering Physics', 'Engineering Physics'), ('Chemical Science and Technology', 'Chemical Science and Technology'), ('Mathematics and Computing', 'Mathematics and Computing'), ('Humanities and Social Sciences', 'Humanities and Social Sciences')], default='Self', max_length=45),
        ),
        migrations.AlterField(
            model_name='task',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2021, 7, 15, 7, 54, 1, 956256, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2021, 7, 15, 7, 54, 1, 956256, tzinfo=utc)),
        ),
    ]
