# Generated by Django 4.0.4 on 2022-04-13 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_alter_note_due_by_alter_note_note_text'),
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
