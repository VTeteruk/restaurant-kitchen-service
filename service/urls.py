from django.urls import path

from service.views import (
    IndexView,
    CookListView,
    DishTypeListView,
    DishListView,
    CookCreateView,
    CookDetailView,
    CookDeleteView,
    CookUpdateView,
    DishCreateView,
    DishDetailView,
    DishDeleteView,
    DishUpdateView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("cook/", CookListView.as_view(), name="cooks-list"),
    path("cook/create/", CookCreateView.as_view(), name="cook-create"),
    path(
        "cook/detail/<int:pk>/", CookDetailView.as_view(), name="cook-detail"
    ),
    path(
        "cook/delete/<int:pk>/", CookDeleteView.as_view(), name="cook-delete"
    ),
    path(
        "cook/update/<int:pk>/", CookUpdateView.as_view(), name="cook-update"
    ),
    path("dish_type/", DishTypeListView.as_view(), name="dish-types-list"),
    path("dish/", DishListView.as_view(), name="dishes-list"),
    path("dish/create/", DishCreateView.as_view(), name="dish-create"),
    path(
        "dish/detail/<int:pk>/", DishDetailView.as_view(), name="dish-detail"
    ),
    path(
        "dish/delete/<int:pk>/", DishDeleteView.as_view(), name="dish-delete"
    ),
    path(
        "dish/update/<int:pk>/", DishUpdateView.as_view(), name="dish-update"
    ),
]

app_name = "service"
