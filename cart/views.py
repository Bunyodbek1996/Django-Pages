from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class Cart(TemplateView):
    template_name = "cart.html"
