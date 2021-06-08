from decimal import *
from django.db.models import Sum, FloatField
from .models import Statistic
from django.utils.dateparse import parse_date
import datetime
from django.db.models import F


def _order_util(start, end, order):
    """
    group_by answer with sum and additional calculations in db
    """
    start_date = parse_date(start)
    end_date = parse_date(end) + datetime.timedelta(days=1)

    if order:
        qs = Statistic.objects.filter(
            date__gte=start_date, date__lte=end_date
        ).values('date').annotate(
            tot_view=Sum('views'),
            tot_clicks=Sum('clicks'),
            tot_cost=Sum('cost')
        ).annotate(
            cpc=F('tot_cost') / F('clicks'),
            cpm=(F('tot_cost') / F('tot_view') * 1000)
        ).order_by(str(order))

    else:
        qs = Statistic.objects.filter(
            date__gte=start_date, date__lte=end_date
        ).values('date').annotate(
            tot_view=Sum('views'),
            tot_clicks=Sum('clicks'),
            tot_cost=Sum('cost')
        ).annotate(
            cpc=F('tot_cost') / F('clicks'),
            cpm=(F('tot_cost') / F('tot_view') * 1000)
        )

    return qs


def data_query_for_time(start, end, order):
    """
    getting data from db Table Statistics and creating serialization in format + adding calculations
    for additional data :
    cpc = cost / clicks (average click price)
    cpm = cost / views * 1000 (average cost 1000 views)
    user can get ordered qs
    """
    qs = _order_util(start, end, order)

    my_qs = []
    for obj in qs:
        my_qs.append({
            "date": obj['date'],
            "total_view": obj['tot_view'],
            "tot_clicks": obj['tot_clicks'],
            "tot_cost": obj['tot_cost'],
            "cpc": obj['cpc'],
            "cpm": obj['cpm'],
        })
    return my_qs


def entry_data_is_valid(date, views, clicks, cost):
    """
    additional data validation
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
