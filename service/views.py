from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views import generic

from service.forms import CookForm
from service.models import DishType, Dish


class IndexView(generic.TemplateView):
    template_name = "service/index.html"
    extra_context = {
        "dish_type_list_count": DishType.objects.count(),
        "dish_list_count": Dish.objects.count(),
        "cook_list_count": get_user_model().objects.count()
    }


class CookListView(generic.ListView):
    model = get_user_model()
    template_name = "service/cook_list.html"
    paginate_by = 5
    extra_context = {
        "full_number_of_cooks": get_user_model().objects.count()
    }


class CookCreateView(generic.CreateView):
    model = get_user_model()
    form_class = CookForm
    template_name = "service/cook_create.html"
    success_url = reverse_lazy("login")


class DishTypeListView(generic.ListView):
    model = DishType
    template_name = "service/dish_type_list.html"
    context_object_name = "dish_type_list"
    paginate_by = 5


class DishListView(generic.ListView):
    model = Dish
    template_name = "service/dish_list.html"
    extra_context = {
        "cook_list_count": get_user_model().objects.count()
    }
    paginate_by = 5
