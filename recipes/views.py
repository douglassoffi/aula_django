from django.shortcuts import render, get_list_or_404, get_object_or_404
from recipes.models import Recipe

def home(request):
    recipes = Recipe.objects.filter(
        is_published=True,
        ).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
        'title': 'Home',
    })

def category(request, category_id):
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id, 
            is_published=True,
        ).order_by('-id')
    )
    return render(request, 'recipes/pages/category.html', context={
    'recipes': recipes,
    'title': f'{recipes[0].category.name} - Categoria',
    })

def recipe(request, id):
    # recipe = get_object_or_404(
    #     Recipe.objects.get(
    #         id=id,
    #     )
    # )
    recipe = Recipe.objects.get(
        id=id,
    )
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'title': recipe.title,
        'is_detail_page': True,
    })
    