# Generated by Django 3.2.12 on 2024-10-04 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_carinstance_mechanic_stat'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='address',
            field=models.TextField(default='Unknown', help_text="What is the customer's address?", max_length=300),
        ),
        migrations.AddField(
            model_name='owner',
            name='has_insurance',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='owner',
            name='insurance_policy_number',
            field=models.CharField(blank=True, default='Unknown', max_length=50),
        ),
        migrations.AddField(
            model_name='owner',
            name='insurance_provider',
            field=models.CharField(blank=True, default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='owner',
            name='phone_num',
            field=models.CharField(default='Unknown', help_text="What is the customer's phone number", max_length=11),
        ),
        migrations.AlterUniqueTogether(
            name='owner',
            unique_together={('first_name', 'last_name', 'phone_num')},
        ),
    ]
