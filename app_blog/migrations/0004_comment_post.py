# Generated by Django 4.1.1 on 2023-04-02 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0003_comment_series_tag_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app_blog.post'),
            preserve_default=False,
        ),
    ]
