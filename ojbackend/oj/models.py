from django.db import models
from django.db.models import Sum


class Underlying(models.Model):
    type_choices = [
        ("STK", "Stock"),
        ("ETF", "Exchange Traded Fund"),
        ("FTR", "Futures"),
    ]
    underlying_type = models.CharField(max_length=50, choices=type_choices)
    ticker_symbol = models.CharField(max_length=20)

    def __str__(self):
        return self.ticker_symbol


class Strategy(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Trade(models.Model):
    STATUSES = [("OP", "Open"), ("CL", "Closed")]
    created_date = models.DateField(auto_now_add=True)
    trade_executed_date = models.DateField()
    trade_close_date = models.DateField(editable=False, null=True, blank=True)
    trade_name = models.CharField(max_length=100, null=True, blank=True)
    strategy = models.ForeignKey(Strategy, on_delete=models.PROTECT)
    description = models.CharField(max_length=255, null=True, blank=True)
    underlying = models.ForeignKey(Underlying, on_delete=models.PROTECT)
    status = models.CharField(
        choices=STATUSES, max_length=10, editable=False, default="OP"
    )

    def __str__(self):
        return f"{self.underlying}-{self.strategy}-{self.id}"

    @property
    def trade_total(self):
        return Trade.objects.filter(trade_set__trade=self).aggregate(
            total=Sum("trade_set__amount")
        )["total"]


class TradeAction(models.Model):
    action_choices = [
        ("INT", "Initial"),
        ("ADJ", "Adjustment"),
        ("CLS", "Close"),
    ]
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    action_executed_date = models.DateField()
    trade = models.ForeignKey(Trade, on_delete=models.CASCADE, related_name="trade_set")
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    action_type = models.CharField(max_length=50, choices=action_choices)

    def __str__(self):
        return f"{self.trade}-{self.action_type}"
