# Generated by Django 3.2.16 on 2023-09-03 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_alter_follow_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together=set(),
        ),
    ]
