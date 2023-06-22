from django.urls import path

from service.views import IndexView, CookViewList, DishTypeList

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("cook/", CookViewList.as_view(), name="cooks-list"),
    path("dish_types/", DishTypeList.as_view(), name="dish-types-list"),
]

app_name = "service"
