# Generated by Django 3.1.7 on 2021-03-05 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_blog_field4'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='field6',
            field=models.CharField(default='', max_length=255),
        ),
    ]
