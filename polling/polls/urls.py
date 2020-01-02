from django.urls import path
from . import views

# URLconf - calls the view and maps it to a URL
urlpatterns = [
    path('', views.index, name='index'),
]
