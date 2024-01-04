from django.urls import path
from . import views
from .views import evaluate_expressions

urlpatterns = [
    path('evaluate/', evaluate_expressions, name='evaluate_expressions'),

]
