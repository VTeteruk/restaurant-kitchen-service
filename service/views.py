from django.contrib.auth import get_user_model
from django.db.models import QuerySet
from django.urls import reverse_lazy
from django.views import generic

from service.forms import CookForm, CookSearchForm
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

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(CookListView, self).get_context_data(**kwargs)

        username = self.request.GET.get("username")

        context["search_form"] = CookSearchForm(initial={"username": username})

        return context

    def get_queryset(self) -> QuerySet:
        self.queryset = get_user_model().objects.all()
        username = self.request.GET.get("username")

        if username:
            return self.queryset.filter(username__icontains=username)
        return self.queryset.all()


class CookCreateView(generic.CreateView):
    model = get_user_model()
    form_class = CookForm
    template_name = "service/cook_create.html"
    success_url = reverse_lazy("login")


class CookDetailView(generic.DetailView):
    model = get_user_model()
    template_name = "service/cook_detail.html"


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
