# Generated by Django 3.0.4 on 2020-03-29 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oj', '0004_auto_20200329_0642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tradeaction',
            name='trade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trade_actions', to='oj.Trade'),
        ),
    ]
