from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


class CreteEntry(APITestCase):

    def test_data(self):
        data = {
            "views": 3,
            "clicks": 4,
            "cost": 15.36,
            "date": "2021-7-10"
        }
        url = reverse('statistic:create')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class SeeStatsByDate(APITestCase):

    def test_stats(self):
        data = {
            "start_date": "2021-6-1",
            "end_date": "2021-6-10",
            "order": "clicks"
        }
        url = reverse('statistic:list')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)


class DeleteAllEntryes(APITestCase):

    def test_delete_all(self):
        data = {"answer": "yes"}
        url = reverse('statistic:remove')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
