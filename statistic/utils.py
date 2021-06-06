import re
from .models import Statistic
from django.db.models import Q
from django.core import serializers


def _order_util(order, start, end):
    """
    return qs in order
    """
    if order:
        qs_actual = Statistic.objects.filter(
            Q(date__gte=start) | Q(date__lte=end)
        ).order_by(str(order))

        return qs_actual


def data_query_for_time(start, end, order):
    """
    getting data from db Table Statistics and creating serialization in format + adding calculations
    for additional data :
    cpc = cost / clicks (average click price)
    cpm = cost / views * 1000 (average cost 1000 views)

    user can get ordered qs
    """

    if order:
        qs_actual = _order_util(order, start, end)
    else:
        qs_actual = Statistic.objects.filter(
            Q(date__gte=start) | Q(date__lte=end)
        )

    print(Statistic.objects.filter(date__gte=start))

    # serializing query
    ser_qs = serializers.serialize('python', qs_actual)
    print(ser_qs)

    # generating appropriate format + additional calculation addons
    my_qs = []
    for i in ser_qs:
        cpc = i['fields']['cost'] / i['fields']['clicks']
        cpm = i['fields']['cost'] / i['fields']['views'] * 1000

        my_qs.append({
            "date": i['fields']['date'],
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
    if date:
        year, month, day = date.split('-')
        if int(year) < 2010 or 12 < int(month) < 1 or 31 < int(day) < 1:
            return True

    # cost cents accuracy (in dolor can't be more than 99 cents)
    if cost:
        cents = int(str(cost).split('.')[1])
        if cents > 99:
            return True
