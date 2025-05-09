from django.shortcuts import render, redirect, get_object_or_404
from .models import Menu, Plats
from .forms import MenuForm, PlatsForm

# Pages de base
def home(request):
    menus = Menu.objects.all()
    return render(request, 'restaurant/home.html', {'menus': menus})

def about(request):
    return render(request, 'restaurant/about.html')

def contact(request):
    return render(request, 'restaurant/contact.html')

# Gestion des menus
def menu_list(request):
    menus = Menu.objects.all()
    return render(request, 'restaurant/menu_list.html', {'menus': menus})

def menu_create(request):
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
    else:
        form = MenuForm()
    return render(request, 'restaurant/menu_form.html', {'form': form})

def menu_update(request, menu_id):
    menu = get_object_or_404(Menu, id=menu_id)
    if request.method == 'POST':
        form = MenuForm(request.POST, instance=menu)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
    else:
        form = MenuForm(instance=menu)
    return render(request, 'restaurant/menu_form.html', {'form': form})

def menu_delete(request, menu_id):
    menu = get_object_or_404(Menu, id=menu_id)
    menu.delete()
    return redirect('menu_list')

# Gestion des plats
def plats_list(request):
    plats = Plats.objects.all()
    return render(request, 'restaurant/plats_list.html', {'plats': plats})

def plats_create(request):
    if request.method == 'POST':
        form = PlatsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('plats_list')
    else:
        form = PlatsForm()
    return render(request, 'restaurant/plats_form.html', {'form': form})

def plats_update(request, plats_id):
    plats = get_object_or_404(Plats, id=plats_id)
    if request.method == 'POST':
        form = PlatsForm(request.POST, request.FILES, instance=plats)
        if form.is_valid():
            form.save()
            return redirect('plats_list')
    else:
        form = PlatsForm(instance=plats)
    return render(request, 'restaurant/plats_form.html', {'form': form})

def plats_delete(request, plats_id):
    plats = get_object_or_404(Plats, id=plats_id)
    plats.delete()
    return redirect('plats_list')
