from .models import Trade, TradeAction, Strategy, Underlying
from rest_framework import serializers


class StrategySerializer(serializers.ModelSerializer):
    class Meta:
        model = Strategy
        fields = "__all__"


class UnderlyingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Underlying
        fields = "__all__"


class TradeActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradeAction
        fields = "__all__"


class TradeSerializer(serializers.ModelSerializer):
    underlying = UnderlyingSerializer(read_only=True)
    strategy = StrategySerializer(read_only=True)
    trade_set = TradeActionSerializer(read_only=True, many=True)
    strategy_name = serializers.CharField(source='strategy.name')
    status_display = serializers.CharField(source='get_status_display')

    class Meta:
        model = Trade
        fields = [
            "created_date",
            "trade_executed_date",
            "trade_close_date",
            "trade_name",
            "strategy",
            "strategy_name",
            "description",
            "underlying",
            "status",
            "status_display",
            "trade_total",
            "trade_set",
        ]


class TradeCreateSerializer(serializers.ModelSerializer):
    # underlying = UnderlyingSerializer(read_only=True)
    # strategy = StrategySerializer(read_only=True)
    amount = serializers.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        model = Trade
        fields = [
            "trade_executed_date",
            "trade_name",
            "strategy",
            "description",
            "underlying",
            "status",
            "amount",
        ]

    def create(self, validated_data):
        amount = validated_data.pop("amount")
        trade = Trade.objects.create(**validated_data)
        TradeAction.objects.create(trade=trade, action_type="INT", amount=amount)
        return trade
