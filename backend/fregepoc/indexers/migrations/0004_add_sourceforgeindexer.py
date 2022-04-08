# Generated by Django 4.0.3 on 2022-04-08 19:35

from django.db import migrations, models
import fregepoc.indexers.models


class Migration(migrations.Migration):

    dependencies = [
        ('indexers', '0003_alter_githubindexer_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='SourceforgeIndexer',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID'
                    )
                ),
                (
                    'current_page',
                    models.PositiveIntegerField(
                        default=1,
                        help_text='The last visited page.',
                        verbose_name='current page'
                    )
                ),
            ],
            options={
                'abstract': False,
            },
            bases=(fregepoc.indexers.models.BaseIndexer,),
        ),
    ]
