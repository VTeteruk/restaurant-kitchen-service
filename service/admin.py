from django.contrib import admin
from django.contrib.auth import get_user_model

from service.models import Dish, DishType

admin.site.register(get_user_model())
admin.site.register(Dish)
admin.site.register(DishType)
