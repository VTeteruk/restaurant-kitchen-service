from django.contrib.auth import get_user_model
from django.test import TestCase

from service.models import DishType, Dish


class ModelsTest(TestCase):
    def test_dish_type_str(self) -> None:
        dish_type = DishType.objects.create(name="test")

        self.assertEquals(str(dish_type), dish_type.name)

    def test_dish_str(self) -> None:
        dish = Dish.objects.create(
            name="test",
            description="test_description",
            price=15.5,
            dish_type=DishType.objects.create(name="test_dish_type"),
        )

        self.assertEquals(str(dish), dish.name)

    def test_create_cook(self) -> None:
        username = "test"
        password = "test12345"
        years_of_experience = 20
        cook = get_user_model().objects.create_user(
            username=username,
            password=password,
            years_of_experience=years_of_experience,
        )

        self.assertTrue(cook.check_password(password))
        self.assertEquals(cook.years_of_experience, years_of_experience)
