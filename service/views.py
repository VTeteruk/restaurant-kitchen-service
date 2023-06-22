from django.contrib.auth import get_user_model
from django.views import generic


class IndexView(generic.TemplateView):
    template_name = "service/index.html"


class CookViewList(generic.ListView):
    model = get_user_model()
    template_name = "service/cook_list.html"
