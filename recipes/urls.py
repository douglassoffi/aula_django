from django.urls import path
from recipes.views import *

app_name = 'recipes'

urlpatterns = [
    path('', home, name="home"),
    path('recipe/category/<int:category_id>/', category, name="category"),
    path('recipe/<int:id>/', recipe, name="recipe"),
    path('recipe/search/', lambda request: ..., name="search"),
]
