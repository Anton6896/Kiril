from decimal import *
from .models import Statistic
from django.core import serializers
from django.utils.dateparse import parse_date
import datetime


def _order_util(start, end, order):
    """
    return qs in order if user asked
    !!! because of my not understanding or bug (i opened at repo)
    i to (+ datetime.timedelta(days=1)) to end date
    Django didnt return date_lte !!!!
    """
    start_date = parse_date(start)
    end_date = parse_date(end) + datetime.timedelta(days=1)

    if order:
        qs_actual = Statistic.objects.filter(
            # date__gte=start_date, date__lte=end_date
            date__gte=start_date, date__lte=end_date
        ).order_by(str(order))

        print(qs_actual.query)
    else:
        qs_actual = Statistic.objects.filter(
            date__gte=start_date, date__lte=end_date
        )
    return qs_actual


def data_query_for_time(start, end, order):
    """
    getting data from db Table Statistics and creating serialization in format + adding calculations
    for additional data :
    cpc = cost / clicks (average click price)
    cpm = cost / views * 1000 (average cost 1000 views)
    user can get ordered qs
    """

    qs_actual = _order_util(start, end, order)

    # serializing query
    ser_qs = serializers.serialize('python', qs_actual)

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
    """
    function to check user data at creation of stat obj
    """
    # check positive value
    if views and int(views) < 0:
        return True
    if clicks and int(clicks) < 0:
        return True
    if cost and Decimal(cost) < 0:
        return True
    if date is None:
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
