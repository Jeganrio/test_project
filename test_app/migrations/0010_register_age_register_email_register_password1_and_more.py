# Generated by Django 4.2.1 on 2024-08-31 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0009_remove_register_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='age',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='register',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='register',
            name='password1',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='register',
            name='password2',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='register',
            name='username',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
