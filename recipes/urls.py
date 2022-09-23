from django.urls import path
from recipes.views import *

app_name = 'recipes'

urlpatterns = [
    path('', home, name="home"),
    path('recipe/search/', search, name="search"),
    path('recipe/category/<int:category_id>/', category, name="category"),
    path('recipe/<int:id>/', recipe, name="recipe"),
]
