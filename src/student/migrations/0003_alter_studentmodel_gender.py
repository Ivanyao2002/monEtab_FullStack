# Generated by Django 5.1 on 2024-08-27 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_studentmodel_delete_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='gender',
            field=models.CharField(choices=[('H', 'Homme'), ('F', 'Femme')], default='Homme', max_length=1),
        ),
    ]
