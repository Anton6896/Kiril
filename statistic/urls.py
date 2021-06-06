from django.urls import path
from .views import ShowStatisticsView, RemoveAllStatisticsView, CreateStatisticsView

app_name = 'statistic'

urlpatterns = [
    path('api/create_new', CreateStatisticsView.as_view(), name='create'),
    path('api/show_by_date', ShowStatisticsView.as_view(), name='list'),
    path('api/remove_all', RemoveAllStatisticsView.as_view(), name='remove'),

]
