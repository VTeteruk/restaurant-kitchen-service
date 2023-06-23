from django.contrib.auth import get_user_model
from django.views import generic

from service.models import DishType, Dish


class IndexView(generic.TemplateView):
    template_name = "service/index.html"
    extra_context = {
        "dish_type_list_count": DishType.objects.count(),
        "dish_list_count": Dish.objects.count(),
        "cook_list_count": get_user_model().objects.count()
    }


class CookViewList(generic.ListView):
    model = get_user_model()
    template_name = "service/cook_list.html"


class DishTypeList(generic.ListView):
    model = DishType
    template_name = "service/dish_type_list.html"
    context_object_name = "dish_type_list"


class DishList(generic.ListView):
    model = Dish
    template_name = "service/dish_list.html"
    extra_context = {
        "cook_list_count": get_user_model().objects.count()
    }
