from django.urls import path
from .views import SaveStatisticsView, ShowStatisticsView, RemoveAllStatisticsView

app_name = 'statistic'

urlpatterns = [
    path('api/create_new', SaveStatisticsView.as_view(), name='save'),
    path('api/show_statistics_all', ShowStatisticsView.as_view(), name='list'),
    path('api/remove_all', RemoveAllStatisticsView.as_view(), name='remove'),

]
