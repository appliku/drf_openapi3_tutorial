# Generated by Django 4.0.6 on 2022-07-11 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogpage_intro_blogpage_show_toc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='intro',
            field=models.TextField(blank=True, default=''),
        ),
    ]
