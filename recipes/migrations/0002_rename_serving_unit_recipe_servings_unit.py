# Generated by Django 4.0.5 on 2022-08-29 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='serving_unit',
            new_name='servings_unit',
        ),
    ]