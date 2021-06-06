from rest_framework import serializers
from .models import Statistic


class CreateStatisticSerializer(serializers.ModelSerializer):
    """
    serializer for the creation of Statistic object
    view, clicks, cost is not required
    """
    views = serializers.IntegerField(required=False)
    clicks = serializers.IntegerField(required=False)
    cost = serializers.DecimalField(required=False, max_digits=6, decimal_places=2)

    class Meta:
        model = Statistic
        fields = ('views', 'clicks', 'cost', 'date')

