from django.shortcuts import render
from authors.forms import UserForm

def register(request):
    if request.POST:
        form = UserForm(request.POST)
    else:
        form = UserForm()
    return render(request, 'authors/pages/register.html', context={
        'form':form,
        'title': 'Registre-se'
    })
