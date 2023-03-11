# django urls file
from django.conf.urls.static import static
from django.urls import path

from memz import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
