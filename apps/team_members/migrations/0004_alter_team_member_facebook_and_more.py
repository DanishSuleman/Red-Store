# Generated by Django 4.0.5 on 2022-07-19 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team_members', '0003_alter_team_member_facebook_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team_member',
            name='facebook',
            field=models.TextField(default='https://www.facebook.com/groups/407961892610345/'),
        ),
        migrations.AlterField(
            model_name='team_member',
            name='linkedIn',
            field=models.TextField(default='https://www.linkedin.com/company/javascript-developer'),
        ),
        migrations.AlterField(
            model_name='team_member',
            name='twitter',
            field=models.TextField(default='https://twitter.com/javascript_dev_'),
        ),
    ]
