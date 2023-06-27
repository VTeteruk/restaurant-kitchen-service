from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from service.models import DishType, Dish

COOK_DETAIL_URL = reverse("service:cook-detail", kwargs={"pk": 1})
DISH_DETAIL_URL = reverse("service:dish-detail", kwargs={"pk": 1})
DISH_TYPE_DETAIL_URL = reverse("service:dish-type-detail", kwargs={"pk": 1})


class PublicDetailTest(TestCase):
    def test_cook_login_required(self) -> None:
        response = self.client.get(COOK_DETAIL_URL)

        self.assertEquals(response.status_code, 302)

    def test_dish_login_required(self) -> None:
        response = self.client.get(DISH_DETAIL_URL)

        self.assertEquals(response.status_code, 302)

    def test_dish_type_login_required(self) -> None:
        response = self.client.get(DISH_TYPE_DETAIL_URL)

        self.assertEquals(response.status_code, 302)


class PrivateDetailTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test_username",
            password="test12345",
            years_of_experience=40,
        )
        self.client.force_login(self.user)

        Dish.objects.create(
            name="test_name",
            description="test_description",
            price=20,
            dish_type=DishType.objects.create(name="test"),
        )

        DishType.objects.create(name="test")

    def test_retrieve_cook_details(self) -> None:
        get_user_model().objects.create_user(
            username="test", password="test12345", years_of_experience=1
        )
        response = self.client.get(COOK_DETAIL_URL)

        self.assertEquals(response.status_code, 200)
        self.assertEquals(self.user.id, response.context["cook"].id)

    def test_retrieve_dish_details(self) -> None:
        response = self.client.get(DISH_DETAIL_URL)

        self.assertEquals(response.status_code, 200)

    def test_retrieve_dish_type_details(self) -> None:
        response = self.client.get(DISH_TYPE_DETAIL_URL)

        self.assertEquals(response.status_code, 200)
