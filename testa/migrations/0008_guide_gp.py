# Generated by Django 4.1.4 on 2023-01-29 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testa', '0007_rename_name_guide_nameb'),
    ]

    operations = [
        migrations.AddField(
            model_name='guide',
            name='gp',
            field=models.ImageField(default='Images/practical.png', upload_to=''),
        ),
    ]
