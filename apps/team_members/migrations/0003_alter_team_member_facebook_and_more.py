# Generated by Django 4.0.5 on 2022-07-15 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team_members', '0002_team_member_facebook_team_member_linkedin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team_member',
            name='facebook',
            field=models.TextField(default='www.facebook.com'),
        ),
        migrations.AlterField(
            model_name='team_member',
            name='linkedIn',
            field=models.TextField(default='www.linkedin.com'),
        ),
        migrations.AlterField(
            model_name='team_member',
            name='twitter',
            field=models.TextField(default='www.twitter.com'),
        ),
    ]