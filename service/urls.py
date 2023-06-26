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
    DishTypeCreateView,
    DishTypeDetailView,
    DishTypeDeleteView,
    DishTypeUpdateView,
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
    path(
        "dish_type/create/",
        DishTypeCreateView.as_view(),
        name="dish-type-create"
    ),
    path(
        "dish_type/detail/<int:pk>/",
        DishTypeDetailView.as_view(),
        name="dish-type-detail"
    ),
    path(
        "dish_type/delete/<int:pk>/",
        DishTypeDeleteView.as_view(),
        name="dish-type-delete"
    ),
    path(
        "dish_type/update/<int:pk>/",
        DishTypeUpdateView.as_view(),
        name="dish-type-update"
    ),
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
