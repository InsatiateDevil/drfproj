# Generated by Django 4.2.13 on 2024-08-21 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0004_subscription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='expires_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата окончания подписки'),
        ),
    ]
