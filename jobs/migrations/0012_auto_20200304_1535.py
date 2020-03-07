# Generated by Django 3.0.3 on 2020-03-04 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0011_auto_20200304_1534'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobposting',
            name='category',
        ),
        migrations.AddField(
            model_name='jobposting',
            name='category_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='jobs.Category'),
        ),
    ]