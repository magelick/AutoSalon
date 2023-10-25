from django.http import HttpResponse
from django.views.generic import TemplateView


class NotFoundTemplateView(TemplateView):
    """
    Класс представления 404 ошибки
    """
    template_name = 'shop/error.html'  # Шаблон
    context_object_name = 'errors'  # Данные на шаблоне

    # Обрабатываем ошибку с помощью данной функции
    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except Exception as exc:
            return HttpResponse('exc')
