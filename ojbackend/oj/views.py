from .serializers import (
    TradeActionSerializer,
    TradeSerializer,
    StrategySerializer,
    UnderlyingSerializer,
    TradeCreateSerializer,
)
from .models import Trade, TradeAction, Strategy, Underlying
from rest_framework.generics import ListCreateAPIView, ListAPIView, CreateAPIView


class TradeList(ListAPIView):
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer


class TradeCreate(CreateAPIView):
    queryset = Trade.objects.all()
    serializer_class = TradeCreateSerializer
