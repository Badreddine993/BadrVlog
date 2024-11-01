# Generated by Django 5.1.2 on 2024-10-27 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_blogpost_content_remove_blogpost_subtitle_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpostimage',
            name='image_title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='blogpostimage',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
