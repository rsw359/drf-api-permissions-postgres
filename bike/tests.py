from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Bike


class BikeTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        test_bike = Bike.objects.create(
            name="BMC",
            purchaser=testuser1,
            description="Carbon, Di2, DTSwiss",
            color="powderblue",
        )
        test_bike.save()

    # class 32
    def setUp(self):
        self.client.login(username="testuser1", password="pass")

    def test_bikes_model(self):
        bike = Bike.objects.get(id=1)
        actual_purchaser = str(bike.purchaser)
        actual_name = str(bike.name)
        actual_color = str(bike.color)
        actual_description = str(bike.description)
        self.assertEqual(actual_purchaser, "testuser1")
        self.assertEqual(actual_name, "BMC")
        self.assertEqual(actual_color, "powderblue")
        self.assertEqual(
            actual_description, "Carbon, Di2, DTSwiss"
        )

    def test_get_bike_list(self):
        url = reverse("bike_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        bikes = response.data
        self.assertEqual(len(bikes), 1)
        self.assertEqual(bikes[0]["name"], "BMC")

    def test_get_bike_by_id(self):
        url = reverse("bike_detail", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        bike = response.data
        self.assertEqual(bike["name"], "BMC")

    def test_create_bike(self):
        url = reverse("bike_list")
        data = {"purchaser": 1, "name": "trek", "description": "Madone",'color': 'goldenrod'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        bikes = Bike.objects.all()
        self.assertEqual(len(bikes), 2)
        self.assertEqual(Bike.objects.get(id=2).name, "trek")

    def test_update_bike(self):
        url = reverse("bike_detail", args=(1,))
        data = {
            "purchaser": 1,
            "name": "BMC",
            "description": "Gran Fondo 01.",
            "color": "black",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        bike = Bike.objects.get(id=1)
        self.assertEqual(bike.name, data["name"])
        self.assertEqual(bike.purchaser.id, data["purchaser"])
        self.assertEqual(bike.description, data["description"])
        self.assertEqual(bike.color, data["color"])

    def test_delete_bike(self):
        url = reverse("bike_detail", args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        bikes = Bike.objects.all()
        self.assertEqual(len(bikes), 0)

    # class 32
    def test_authentication_required(self):
        self.client.logout()
        url = reverse("bike_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)