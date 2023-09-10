# Generated by Django 3.2.16 on 2023-09-05 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_alter_follow_unique_together'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('user', 'following'), name='user_following'),
        ),
    ]
