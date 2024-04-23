# Generated by Django 3.2.25 on 2024-04-23 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productvariant',
            name='name',
            field=models.CharField(blank=True, choices=[('s', 's'), ('m', 'm'), ('l', 'l'), ('xl', 'xl'), ('xxl', 'xxl')], max_length=100, null=True),
        ),
    ]