# Generated by Django 5.1.5 on 2025-02-12 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_pdf_file_journalname_journal_template_file_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='journalname',
            old_name='journal_template_file',
            new_name='journal_template_pdf_file',
        ),
        migrations.RenameField(
            model_name='journalname',
            old_name='stylesheet_file',
            new_name='journal_template_word_file',
        ),
        migrations.AddField(
            model_name='journalname',
            name='stylesheet_pdf_file',
            field=models.FileField(default=1, upload_to='uploads/journal'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='journalname',
            name='stylesheet_word_file',
            field=models.FileField(default=1, upload_to='uploads/journal'),
            preserve_default=False,
        ),
    ]
