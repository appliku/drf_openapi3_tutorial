from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
   path('', TemplateView.as_view(
       template_name="main/main.html",
   ), name='main_main'),
]