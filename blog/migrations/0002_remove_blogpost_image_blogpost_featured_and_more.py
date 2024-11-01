# Generated by Django 5.1.2 on 2024-10-26 18:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='image',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='read_time',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='tag',
            field=models.CharField(default='General', max_length=100),
        ),
        migrations.CreateModel(
            name='BlogPostImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='blog_images/')),
                ('alt_text', models.CharField(blank=True, max_length=255, null=True)),
                ('blog_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='blog.blogpost')),
            ],
        ),
    ]
