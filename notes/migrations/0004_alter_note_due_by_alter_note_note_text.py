# Generated by Django 4.0.4 on 2022-04-13 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_alter_category_options_alter_note_due_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='due_by',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='note_text',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
