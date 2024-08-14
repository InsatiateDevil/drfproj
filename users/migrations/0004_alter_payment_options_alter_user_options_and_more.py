# Generated by Django 4.2.13 on 2024-08-14 19:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_alter_lesson_course'),
        ('users', '0003_payment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payment',
            options={'verbose_name': 'платеж', 'verbose_name_plural': 'платежи'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'пользователь', 'verbose_name_plural': 'пользователи'},
        ),
        migrations.AddField(
            model_name='payment',
            name='lesson',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='education.lesson', verbose_name='Оплаченный урок'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Сумма платежа'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.course', verbose_name='Курс'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата оплаты'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='method',
            field=models.CharField(max_length=100, verbose_name='Способ оплаты'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
