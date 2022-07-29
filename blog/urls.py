from django.urls import path
from wagtail.contrib.sitemaps.views import sitemap

app_name = 'blog'
urlpatterns = [
    path('sitemap.xml', sitemap),
]
