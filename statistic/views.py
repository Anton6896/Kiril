from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .models import Statistic
from .utils import data_query_for_time, entry_data_is_valid


class CreateStatisticsView(APIView):
    """
    Creating entry of Statistic obj if data ok
    else have validators that check appropriate values (all data mast be in positive range)
    """
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        # show explanation to user
        msg = 'please enter data in format { ' \
              'views: positive int, ' \
              'clicks: positive int,' \
              'cost: positive decimal,' \
              'date: yyyy-mm-dd } date must be provided '
        return Response({"msg": msg})

    def post(self, request):
        date = request.data.get('date')
        views = request.data.get('views')
        clicks = request.data.get('clicks')
        cost = request.data.get('cost')

        # use custom validator to check positive values
        if entry_data_is_valid(date, views, clicks, cost):
            return Response({"msg": "your data is invalid"}, status=400)

        else:

            # if object created return status 200 with message
            _, created = Statistic.objects.get_or_create(
                views=views,
                clicks=clicks,
                cost=cost,
                date=date
            )
            if created:
                return Response({"msg": "entry created"}, status=201)
            else:
                return Response({"msg": "some server error please tell to admin "}, status=400)


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
            Statistic.objects.all().delete()
            return Response({"msg": "all statistics data was removed"}, status=200)
        else:
            return Response({"msg": "please try again , sys can't understand ypu"}, status=302)
