from django.contrib import admin
from .models import Category, Recipe

@admin.register(Category)
@admin.register(Recipe)

class CategoryAdmin(admin.ModelAdmin):
    ...

class RecipeAdmin(admin.ModelAdmin):
    ...
