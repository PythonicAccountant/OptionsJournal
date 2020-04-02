from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/trades', views.TradeList.as_view()),
    path('api/v1/trade-create', views.TradeCreate.as_view())
]
