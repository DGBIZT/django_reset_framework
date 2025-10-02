from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from users.models import CustomUser
from vehicle.models import Car, Milage

import os
import sys
import django

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_reset_framework.settings')
django.setup()



class VehicleTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(username='admin', password='1234')

    def test_create_car(self):
        """ Тестирование создания машины """

        # Добавляем аутентификацию
        self.client.force_authenticate(user=self.user)

        data = {
            'title': "Test",
            'description': "Автомобиль",
            'milage': [{
                'milage': 0,
                'year': 2025
            }]
        }
        response = self.client.post(
            '/cars/',
            data=data,
            format='json' # Явно указываем формат данных
        )
        response_data = response.json()
        print("Response:", response_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_data['title'], 'Test')
        self.assertEqual(response_data['description'], 'Автомобиль')
        self.assertEqual(len(response_data['milage']), 1)  # Проверяем, что пробег создан
        self.assertEqual(response_data['milage'][0]['milage'], 0)

        self.assertTrue(
            Car.objects.all().exists()
        )



    def test_list_car(self):
        """ Тестирование вывода список машин """

        # Добавляем аутентификацию
        self.client.force_authenticate(user=self.user)

        # Добавляем новую машину
        car = Car.objects.create(
            title="Test",
            description="Автомобиль",
            owner=self.user,
        )
        # Затем создаем пробег для этой машины
        Milage.objects.create(
            car=car,
            milage=0,
            year=2025
        )

        # Делаем GET запрос
        response = self.client.get(
            '/cars/'
        )

        # Проверяем статус ответа
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Получаем данные из ответа
        response_data = response.json()

        # Проверяем количество записей
        self.assertEqual(len(response_data), 1)

        # Проверяем поля первой машины
        car_data = response_data[0]
        self.assertEqual(car_data['title'], 'Test')
        self.assertEqual(car_data['description'], 'Автомобиль')

        # Проверяем пробег
        milage_data = car_data['milage'][0]
        self.assertEqual(milage_data['milage'], 0)
        self.assertEqual(milage_data['year'], 2025)

        # Проверяем связи
        self.assertEqual(car_data['owner'], self.user.id)
        self.assertEqual(car_data['last_milage'], 0)