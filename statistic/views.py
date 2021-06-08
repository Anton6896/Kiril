from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .models import Statistic
from .utils import data_query_for_time
from rest_framework.generics import CreateAPIView
from .serializers import CreateStatisticsSerializer
from django.db import connection


class CreateStatisticsView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = CreateStatisticsSerializer(data=request.data)
        if serializer.is_valid():
            Statistic.objects.create(
                views=request.data.get('views'),
                clicks=request.data.get('clicks'),
                cost=request.data.get('cost'),
                date=request.data.get('date')
            )
            return Response({"msg": "created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShowStatisticsView(APIView):
    """
    get :: show to user format that he need to enter date for creating queries
    post :: grub data, make query , add calculation , return asked formatting
    on post user can specify order to show
    """
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        msg = 'please enter data in format {start_date:date,end_date:date, order:optional }' \
              ' date format is yyyy-mm-dd'
        return Response({"msg": msg})

    def post(self, request):
        """
        get from user range of time for creating appropriate query
        """
        start_date = request.data.get('start_date')
        end_date = request.data.get('end_date')
        order = request.data.get('order')
        js_data = data_query_for_time(start_date, end_date, order)

        # response to user
        if js_data:
            return Response({"data": js_data}, status=200)
        else:
            return Response({"msg": "no data"}, status=404)


class RemoveAllStatisticsView(APIView):
    """
    Removes all saved statistics.
    user must post {"answer": "yes"}
    """
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        msg = 'do you like to remove all statistics data ? please enter in format {"answer": "yes"}'
        return Response({"msg": msg})

    def post(self, request):
        answer: str = request.data.get("answer")
        if answer.lower() == "yes":
            # Statistic.objects.truncate()
            cursor = connection.cursor()
            # for sqlite using DELETE FROM
            cursor.execute("DELETE FROM `statistic`")

            return Response({"msg": "all statistics data was removed"}, status=200)
        else:
            return Response({"msg": "please try again , sys can't understand ypu"}, status=400)
