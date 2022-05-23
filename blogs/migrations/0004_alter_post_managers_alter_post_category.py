# Generated by Django 4.0.4 on 2022-05-12 20:00

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_alter_post_published'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='post',
            managers=[
                ('get_published_posts', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='blogs.category'),
        ),
    ]