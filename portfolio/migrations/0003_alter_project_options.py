# Generated by Django 4.1.2 on 2022-10-20 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_project_link_alter_project_created_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-created'], 'verbose_name': 'Proyecto', 'verbose_name_plural': 'Proyectos'},
        ),
    ]
