# Generated by Django 4.1.7 on 2023-04-02 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reader', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reader',
            name='is_admin',
        ),
        migrations.AddField(
            model_name='reader',
            name='role',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Владелец'), (2, 'Админ')], default=1, verbose_name='Роль'),
        ),
    ]
