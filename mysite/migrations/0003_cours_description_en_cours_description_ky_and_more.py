# Generated by Django 5.0.6 on 2024-07-02 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_rename_descriptionm_department_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cours',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='cours',
            name='description_ky',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='cours',
            name='description_ru',
            field=models.TextField(null=True),
        ),
    ]
