from .models import Statistic
from django.db.models import Q
from django.core import serializers


def data_query_for_time(start, end):
    qs_actual = Statistic.objects.filter(
        Q(date__gte=start) & Q(date__lte=end)
    )

    qs = Statistic.objects.all()

    ser_qs = serializers.serialize('python', qs)

    for i in ser_qs:
        print(i['fields'])

    return " "
