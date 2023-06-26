from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.urls import reverse_lazy
from django.views import generic

from service.forms import CookForm, CookSearchForm, DishForm, DishSearchForm, \
    DishTypeSearchForm
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
    template_name = "service/cook_form.html"
    success_url = reverse_lazy("login")


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = get_user_model()
    template_name = "service/cook_detail.html"


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = get_user_model()
    template_name = "service/cook-delete.html"
    success_url = reverse_lazy("service:cooks-list")


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = get_user_model()
    template_name = "service/cook_form.html"
    success_url = reverse_lazy("service:cooks-list")
    fields = ("username", "first_name", "last_name", "years_of_experience")


class DishTypeListView(generic.ListView):
    model = DishType
    template_name = "service/dish_type_list.html"
    context_object_name = "dish_type_list"
    extra_context = {
        "full_number_of_dish_types": DishType.objects.count()
    }
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(DishTypeListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = DishTypeSearchForm(initial={"name": name})
        return context

    def get_queryset(self) -> QuerySet:
        self.queryset = DishType.objects.all()
        name = self.request.GET.get("name")

        if name:
            return self.queryset.filter(name__icontains=name)
        return self.queryset


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = "__all__"
    template_name = "service/dish_type_form.html"
    success_url = reverse_lazy("service:dish-types-list")


class DishTypeDetailView(LoginRequiredMixin, generic.DetailView):
    model = DishType
    fields = "__all__"
    template_name = "service/dish_type_detail.html"


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    template_name = "service/dish_type_delete.html"
    success_url = reverse_lazy("service:dish-types-list")


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = "__all__"
    template_name = "service/dish_type_form.html"
    success_url = reverse_lazy("service:dish-types-list")


class DishListView(generic.ListView):
    model = Dish
    template_name = "service/dish_list.html"
    extra_context = {
        "full_number_of_cooks": Dish.objects.count()
    }
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        context = super(DishListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = DishSearchForm(initial={"name": name})
        return context

    def get_queryset(self) -> QuerySet:
        self.queryset = Dish.objects.all().select_related("dish_type")
        name = self.request.GET.get("name")

        if name:
            return self.queryset.filter(name__icontains=name)
        return self.queryset.all()


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    form_class = DishForm
    template_name = "service/dish_form.html"
    success_url = reverse_lazy("service:dishes-list")


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish
    template_name = "service/dish_detail.html"


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    template_name = "service/dish_delete.html"
    success_url = reverse_lazy("service:dishes-list")


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    template_name = "service/dish_form.html"
    success_url = reverse_lazy("service:dishes-list")
    form_class = DishForm
