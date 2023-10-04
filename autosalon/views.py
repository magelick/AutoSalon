from django.http import HttpResponse
from django.views.generic import TemplateView


class NotFoundTemplateView(TemplateView):
    template_name = 'shop/error.html'
    context_object_name = 'errors'

    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except Exception as exc:
            return HttpResponse('exc')
