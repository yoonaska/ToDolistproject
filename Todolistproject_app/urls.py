import fractions
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('delete/<int:id>', views.Delete, name='Delete'),
    path('uncomplete/<int:id>', views.incomplete, name='incomplete'),
    path('complete/<int:id>', views.complete, name='complete'),
]