# coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse_lazy

from django.views.generic import View, TemplateView, CreateView


from .forms import Contactform

User = get_user_model()

class indexView(TemplateView):
    template_name = 'index.html'


index = indexView.as_view()


def contact(request):
    success = False
    form = Contactform(request.POST or None)

    if form.is_valid():
        form.send_email()
        success = True

    context = {
        'form': form,
        'success': success
    }

    return render(request, 'contact.html', context)

