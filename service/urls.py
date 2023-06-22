from django.urls import path

from service.views import IndexView, CookViewList

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("cook/", CookViewList.as_view(), name="cooks-list"),
]

app_name = "service"
