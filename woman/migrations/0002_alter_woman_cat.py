# Generated by Django 4.1.5 on 2023-01-20 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('woman', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='woman',
            name='cat',
            field=models.ForeignKey(default='Фея', null=True, on_delete=django.db.models.deletion.PROTECT, to='woman.category'),
        ),
    ]
