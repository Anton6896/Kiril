from django.urls import path
from .views import (ShowStatisticsView, RemoveAllStatisticsView,
                    CreateStatisticsView)

app_name = 'statistic'

urlpatterns = [
    path('create', CreateStatisticsView.as_view(), name='create'),
    path('show_by_date', ShowStatisticsView.as_view(), name='list'),
    path('remove_all', RemoveAllStatisticsView.as_view(), name='remove'),
]
