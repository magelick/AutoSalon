from django.views.generic import TemplateView
from .forms import ContactForm
from .tasks import send_message_of_the_autosalon
from django.shortcuts import render


class ShopListView(TemplateView):
    template_name = 'shop/index.html'
    context_object_name = 'shop'


class AboutUsTemplateView(TemplateView):
    template_name = 'shop/about.html'


class ContactTemplateView(TemplateView):
    template_name = 'shop/contact.html'
    context_object_name = 'contact'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContactForm()
        return context

    def post(self, request):
        form = ContactForm(request.POST)

        if form.is_valid():
            send_message_of_the_autosalon.delay(
                subject=form.cleaned_data['topic_of_the_question'],
                message=form.cleaned_data['question'],
                from_email=form.cleaned_data['email']
            )
        else:
            return render(
                request=request,
                template_name=self.template_name,
                context={'form': form}
            )
