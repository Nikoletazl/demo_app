from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from demo_app.web.models import Item


class IndexView(TemplateView):
    model = Item
    template_name = 'index.html'