from django.views import generic as views

from demo_app.web.models import Item


class IndexView(views.ListView):
    template_name = 'index.html'
    model = Item