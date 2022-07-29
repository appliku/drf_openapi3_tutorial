# Generated by Django 4.0.6 on 2022-07-11 09:10

from django.db import migrations, models
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogtag_article_alter_blogpagetag_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='intro',
            field=wagtail.fields.RichTextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='show_toc',
            field=models.BooleanField(default=True, verbose_name='Show Table of Contents'),
        ),
    ]