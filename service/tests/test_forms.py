from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from service.models import Dish, DishType


class CreateCookTest(TestCase):
    def test_create_cook(self) -> None:
        form_data = {
            "username": "test_username",
            "password1": "test12345",
            "password2": "test12345",
            "first_name": "test_first_name",
            "last_name": "test_last_name",
            "years_of_experience": 25
        }

        self.client.post(reverse("service:cook-create"), data=form_data)
        new_user = get_user_model().objects.get(
            username=form_data.get("username")
        )

        self.assertEquals(new_user.username, form_data["username"])
        self.assertEquals(new_user.first_name, form_data["first_name"])
        self.assertEquals(new_user.last_name, form_data["last_name"])
        self.assertEquals(
            new_user.years_of_experience,
            form_data["years_of_experience"]
        )


class PublicCreateDishAndDishTypeTest(TestCase):
    def test_create_dish_type(self) -> None:
        form_data = {
            "name": "test_name"
        }

        self.client.post(reverse("service:dish-type-create"), data=form_data)

        self.assertEquals(DishType.objects.count(), 0)

    def test_create_dish(self) -> None:
        form_data = {
            "name": "test_name",
            "description": "test_description",
            "price": 25,
            "dish_type": DishType.objects.create(name="name")
        }

        self.client.post(reverse("service:dish-create"), data=form_data)

        self.assertEquals(Dish.objects.count(), 0)


class PrivateCreateDishAndDishTypeTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test12345",
            years_of_experience=25
        )

        self.client.force_login(self.user)

    def test_create_dish(self) -> None:
        dish_type = DishType.objects.create(name="test")
        cook = get_user_model().objects.get(username=self.user.username)

        form_data = {
            "name": "test",
            "description": "test",
            "price": 25,
            "dish_type": dish_type.id,
            "cooks": [cook.id]
        }

        self.client.post(reverse("service:dish-create"), data=form_data)
        new_dish = Dish.objects.get(name=form_data["name"])

        self.assertEquals(new_dish.name, form_data["name"])
        self.assertEquals(new_dish.description, form_data["description"])
        self.assertEquals(new_dish.price, form_data["price"])
        self.assertEquals(new_dish.dish_type, dish_type)
        self.assertEquals(list(new_dish.cooks.all()), [cook])

    def test_create_dish_type(self) -> None:
        form_data = {
            "name": "test_name"
        }

        self.client.post(reverse("service:dish-type-create"), data=form_data)
        new_dish_type = DishType.objects.get(
            name=form_data.get("name")
        )

        self.assertEquals(new_dish_type.name, form_data["name"])
