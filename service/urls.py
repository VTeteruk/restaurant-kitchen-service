from django.urls import path

from service.views import IndexView, CookViewList, DishTypeList, DishList

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("cook/", CookViewList.as_view(), name="cooks-list"),
    path("dish_type/", DishTypeList.as_view(), name="dish-types-list"),
    path("dish/", DishList.as_view(), name="dishes-list"),
]

app_name = "service"
