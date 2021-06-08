from rest_framework.test import APITestCase
from django.urls import reverse
from django.db import connection
from .models import Statistic


class CreteEntry(APITestCase):

    def test_data(self):
        url = reverse('statistic:create')
        data = {
            "views": 3,
            "clicks": 4,
            "cost": 15.36,
            "date": "2021-7-10"
        }

        # create entry in db
        response = self.client.post(url, data)

        # check if entry in db
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM `statistic` WHERE views = 3")

        row = None
        for i in cursor:
            row = i
        self.assertTrue(3 in row)


class SeeStatsByDate(APITestCase):

    def test_stats(self):
        # crete obj
        Statistic.objects.create(
            views=2,
            clicks=2,
            cost=22.2,
            date="2021-6-3"
        )

        # look for data in db
        data = {
            "start_date": "2021-6-3",
            "end_date": "2021-6-5",
            "order": "clicks"
        }
        url = reverse('statistic:list')
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)


class DeleteAlLTableData(APITestCase):

    def test_delete_all(self):
        # create entry
        Statistic.objects.create(
            views=2,
            clicks=2,
            cost=22.2,
            date="2021-6-3"
        )

        # delete all
        data = {"answer": "yes"}
        url = reverse('statistic:remove')
        response = self.client.post(url, data)

        # check if db empty
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM `statistic`")

        row = None
        for i in cursor:
            row = i

        self.assertTrue(row is None)

# ================================
