# Generated by Django 4.0 on 2024-04-16 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='status',
            field=models.CharField(choices=[('DR', 'Darft'), ('PB', 'Published')], default='DR', max_length=2),
        ),
    ]
