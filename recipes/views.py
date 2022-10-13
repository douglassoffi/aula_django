from django.shortcuts import render, get_list_or_404, get_object_or_404
from recipes.models import Recipe
from django.http import Http404
from django.db.models import Q
from utils.pagination import make_pagination

def home(request):
    recipes = Recipe.objects.filter(
        is_published=True,
    ).order_by('-id')

    page_obj, pagination_range =  make_pagination(
        request, 
        object_list=recipes, 
    )

    return render(request, 'recipes/pages/home.html', context={
        'recipes': page_obj,
        'pagination_range': pagination_range,
        'title': 'Home',
    })

    Paginator(object_list, per_page)

def category(request, category_id):
    recipes = get_list_or_404(Recipe.objects.filter(
        category__id=category_id,
        is_published=True,
    ).order_by('-id'))

    page_obj, pagination_range =  make_pagination(
        request, 
        object_list=recipes, 
    )

    return render(request, 'recipes/pages/category.html', context={
    'recipes': page_obj,
    'pagination_range': pagination_range,
    'title': f'{recipes[0].category.name} - Categoria',
    })

def recipe(request, id):
    recipe = get_object_or_404(Recipe.objects.filter(
        id=id, 
        is_published=True,
    ))
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'title': recipe.title,
        'is_detail_page': True,
    })
    
def search(request):
    term = request.GET.get('q', '').strip()
    if not term:
        raise Http404()
    recipes = Recipe.objects.filter(
        Q(
            Q(title__icontains=term) | 
            Q(description__icontains=term)
        ),
        is_published=True,
    ).order_by('-id')

    page_obj, pagination_range =  make_pagination(
        request, 
        object_list=recipes, 
    )

    return render(request, 'recipes/pages/search-view.html', context={
        'recipes': page_obj,
        'pagination_range': pagination_range,
        'title': f'"{term}"',
        'term': term,
        'additional_url_query': f'&q={term}',
    })
