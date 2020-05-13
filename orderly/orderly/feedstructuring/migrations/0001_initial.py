# Generated by Django 3.0.6 on 2020-05-12 23:51

from django.db import migrations, models
import django.db.models.deletion
import feedstructuring.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chorescheduling', '0003_auto_20200512_2351'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('uuid', models.AutoField(primary_key=True, serialize=False)),
                ('action', models.IntegerField(choices=[(feedstructuring.models.Notification.ACTIONS['COMPLETED'], 'Completed'), (feedstructuring.models.Notification.ACTIONS['CHANGED'], 'Changed')], default=feedstructuring.models.Notification.ACTIONS['COMPLETED'])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('chore_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chorescheduling.ChoreInfo')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]