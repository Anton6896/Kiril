from django.shortcuts import render
from rest_framework.renderers import JSONRenderer

from rest_framework.generics import (
    CreateAPIView
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import CreateStatisticSerializer
from .models import Statistic

from .utils import data_query_for_time


class SaveStatisticsView(CreateAPIView):
    """
    create statistics entry
    """
    queryset = Statistic.objects.all()
    serializer_class = CreateStatisticSerializer


class ShowStatisticsView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        msg = 'please enter data in format {start_date:date,end_date:date } date format is yyyy-mm-dd'
        return Response({"msg": msg})

    def post(self, request):
        """
        get from user range of time for creating appropriate query
        """
        start_date = request.data.get('start_date')
        end_date = request.data.get('start_date')

        js_data = data_query_for_time(start_date, end_date)

        # response to user
        if js_data:
            return Response({"data": js_data}, status=200)
        else:
            return Response({"msg": "no data"}, status=404)


def reset_statistics():
    pass
