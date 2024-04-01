from django.urls import path
from . import views

urlpatterns = [
    path('ToDo/', views.vw_ToDo, name='to_do_view'),
]