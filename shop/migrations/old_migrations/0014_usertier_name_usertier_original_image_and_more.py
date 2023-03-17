# Generated by Django 4.1.2 on 2023-03-15 16:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("shop", "0013_rename_photothumbnail_thumbnail_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="usertier",
            name="name",
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AddField(
            model_name="usertier",
            name="original_image",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="thumbnail",
            name="photo_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="thumbnail",
                to="shop.photo",
            ),
        ),
        migrations.AlterField(
            model_name="usertier",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]