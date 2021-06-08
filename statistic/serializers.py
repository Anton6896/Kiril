from rest_framework import serializers
from .models import Statistic
from rest_framework.validators import ValidationError


class CreateStatisticsSerializer(serializers.ModelSerializer):
    date = serializers.DateField(format="%Y-%m-%d")
    views = serializers.IntegerField(required=False)
    clicks = serializers.IntegerField(required=False)
    cost = serializers.DecimalField(required=False, max_digits=6, decimal_places=2)

    class Meta:
        model = Statistic
        fields = ('views', 'clicks', 'cost', 'date')

    def validate_views(self, views):
        if views and views < 0:
            raise ValidationError('views must be > 0')

    def validate_clicks(self, clicks):
        if clicks and clicks < 0:
            raise ValidationError('clicks must be > 0')

    def validate_cost(self, cost):
        if cost and cost < 0:
            raise ValidationError('cost must be > 0')
