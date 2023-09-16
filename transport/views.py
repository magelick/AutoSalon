from django.views.generic import ListView, TemplateView
from .models import AnnouncementCar
# from .forms import SearchCarsForm


class CarSearchListView(ListView):
    model = AnnouncementCar
    template_name = 'transport/search_form.html'
    context_object_name = 'search_car'

    def get_queryset(self):
        queryset = AnnouncementCar.objects.all()
        return queryset

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     form = SearchCarsForm(self.request.GET)
    #     context['form'] = form
    #     return context


class NotFoundTemplateView(TemplateView):
    template_name = 'transport/404.html'
