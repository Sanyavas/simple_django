# Generated by Django 5.0 on 2023-12-31 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='picture',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
