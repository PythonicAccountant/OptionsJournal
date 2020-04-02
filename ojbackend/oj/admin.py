from django.contrib import admin
from .models import Trade, TradeAction, Underlying, Strategy

# Register your models here.
admin.site.register(Trade)
admin.site.register(TradeAction)
admin.site.register(Underlying)
admin.site.register(Strategy)
