from django.shortcuts import render, redirect
from authors.forms import RegisterForm
from django.http import Http404
from django.contrib import messages
from django.urls import reverse

def register(request):
    register_form_data = request.session.get('register_form_data')
    form = RegisterForm(register_form_data)
    
    return render(request, 'authors/pages/register.html', context={
        'form': form,
        'form_action': reverse('authors:create'),
        'title': 'Registre-se'
    })

def register_create(request):
    if not request.POST:
        raise Http404()
        
    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        messages.success(request, 'Usuário criado com sucesso!')
        del(request.session['register_form_data'])
    
    else:
        messages.error(request, 'Verifique os campos!')

    return redirect('authors:register')
