# Generated by Django 5.1.3 on 2025-03-28 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0002_tag_project_vote_ratio_project_vote_total_review_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="featured_image",
            field=models.ImageField(
                blank=True, default="icon.jpg", null=True, upload_to=""
            ),
        ),
    ]
