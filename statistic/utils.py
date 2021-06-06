import re
from .models import Statistic
from django.db.models import Q
from django.core import serializers


def data_query_for_time(start, end):
    """
    getting data from db Table Statistics and creating serialization in format + adding calculations
    for additional data :
    cpc = cost / clicks (average click price)
    cpm = cost / views * 1000 (average cost 1000 views)
    """
    qs_actual = Statistic.objects.filter(
        Q(date__gte=start) & Q(date__lte=end)
    )

    # serializing query
    ser_qs = serializers.serialize('python', qs_actual)

    # generating appropriate format + additional calculation addons
    my_qs = []
    for i in ser_qs:
        date = i['fields']['date']

        cpc = i['fields']['cost'] / i['fields']['clicks']
        cpm = i['fields']['cost'] / i['fields']['views'] * 1000

        my_qs.append({
            "date": date,
            "views": i['fields']['views'],
            "clicks": i['fields']['clicks'],
            "cost": i['fields']['cost'],
            "cpc": cpc,
            "cpm": cpm
        })

    return my_qs


def entry_data_is_valid(date, views, clicks, cost):
    # check positive value
    if views and views < 0:
        return True
    if clicks and clicks < 0:
        return True
    if cost and cost < 0:
        return True

    # check date
    year, month, day = date.split('-')
    if int(year) < 2010 or 12 < int(month) < 1 or 31 < int(day) < 1:
        return True

    # cost cents accuracy (in dolor can't be more than 99 cents)
    if cost:
        cents = int(str(cost).split('.')[1])
        if cents > 99:
            return True

    return False
