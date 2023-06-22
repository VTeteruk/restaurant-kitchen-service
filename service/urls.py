from django.urls import path

urlpatterns = [
    path("", IndexView, name="index")
]