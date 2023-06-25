from django.urls import path

from service.views import IndexView, CookListView, DishTypeListView, DishListView, CookCreateView, CookDetailView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("cook/", CookListView.as_view(), name="cooks-list"),
    path("cook/create/", CookCreateView.as_view(), name="cook-create"),
    path("cook/detail/<int:pk>", CookDetailView.as_view(), name="cook-detail"),
    path("dish_type/", DishTypeListView.as_view(), name="dish-types-list"),
    path("dish/", DishListView.as_view(), name="dishes-list"),
]

app_name = "service"
