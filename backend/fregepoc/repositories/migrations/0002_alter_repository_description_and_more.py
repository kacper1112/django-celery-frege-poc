# Generated by Django 4.0.4 on 2022-04-20 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repositories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repository',
            name='description',
            field=models.TextField(blank=True, default='', help_text='The description of the repository', max_length=2048, verbose_name='Repository description'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='repositoryfile',
            name='repo_relative_file_path',
            field=models.CharField(blank=True, help_text='File path, relative to the repository root.', max_length=512, null=True),
        ),
    ]