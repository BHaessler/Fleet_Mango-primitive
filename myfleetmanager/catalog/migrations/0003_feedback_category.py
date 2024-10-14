# Generated by Django 3.2.12 on 2024-10-14 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='category',
            field=models.CharField(choices=[('site', 'Site Feedback'), ('personnel', 'Personnel Feedback'), ('shop', 'Shop Feedback'), ('general', 'General Feedback')], default='general', max_length=10),
        ),
    ]
