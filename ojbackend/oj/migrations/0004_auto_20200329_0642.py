# Generated by Django 3.0.4 on 2020-03-29 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oj', '0003_auto_20200328_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
