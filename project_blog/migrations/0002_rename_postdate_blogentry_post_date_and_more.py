# Generated by Django 4.2.7 on 2024-02-05 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogentry',
            old_name='postDate',
            new_name='post_date',
        ),
        migrations.RenameField(
            model_name='blogentry',
            old_name='postText',
            new_name='post_text',
        ),
        migrations.RenameField(
            model_name='blogentry',
            old_name='postTitle',
            new_name='post_title',
        ),
    ]
