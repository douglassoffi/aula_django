from django.urls import path
from recipes.views import *

app_name = 'recipes'

urlpatterns = [
    path('', home, name="home"),
    path('recipe/<int:id>/', recipe, name="recipe"),
]
