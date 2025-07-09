from django.shortcuts import render, redirect

# Create your views here.
from item.models import Category, Item
from .forms import SignupForm
from django.contrib.auth import logout


def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'main/index.html', {
        'categories': categories,
        'items': items,
    })


def contact(request):
    return render(request, 'main/contact.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'main/signup.html', {
        'form': form
    })


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/login/')
    return render(request, 'main/logout.html')
