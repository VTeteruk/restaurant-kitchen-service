from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class DishType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(
        validators=[
            MinValueValidator(
                0, message="Years of experience must be a positive number."
            ),
            MaxValueValidator(
                50, message="Years of experience cannot exceed 50."
            ),
        ]
    )

    class Meta:
        ordering = ["username"]


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=5)
    dish_type = models.ForeignKey(
        DishType, on_delete=models.CASCADE, related_name="dishes"
    )
    cooks = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="dishes"
    )

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name
