# Generated by Django 3.0.4 on 2020-03-28 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Strategy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateTimeField()),
                ('trade_executed_date', models.DateField()),
                ('trade_close_date', models.DateField()),
                ('trade_name', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('OP', 'Open'), ('CL', 'Closed')], max_length=10)),
                ('strategy', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='oj.Strategy')),
            ],
        ),
        migrations.CreateModel(
            name='Underlying',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('underlying_type', models.CharField(choices=[('STK', 'Stock'), ('ETF', 'Exchange Traded Fund'), ('FTR', 'Futures')], max_length=50)),
                ('ticker_symbol', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TradeAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('action_type', models.CharField(choices=[('INT', 'Initial'), ('ADJ', 'Adjustment'), ('CLS', 'Close')], max_length=50)),
                ('trade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oj.Trade')),
            ],
        ),
        migrations.AddField(
            model_name='trade',
            name='underlying',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='oj.Underlying'),
        ),
    ]
