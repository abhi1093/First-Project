# Generated by Django 3.0.6 on 2020-05-17 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimage',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='authapp.Post'),
            preserve_default=False,
        ),
    ]
