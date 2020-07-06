# Generated by Django 2.2.13 on 2020-07-06 04:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('write_a_comment', models.TextField(max_length=200)),
                ('art', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='news.News')),
                ('usr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_by_usr', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('art', 'write_a_comment')},
            },
        ),
    ]
