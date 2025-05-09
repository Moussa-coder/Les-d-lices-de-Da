from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('menus/', views.menu_list, name='menu_list'),
    path('menus/create/', views.menu_create, name='menu_create'),
    path('menus/<int:menu_id>/update/', views.menu_update, name='menu_update'),
    path('menus/<int:menu_id>/delete/', views.menu_delete, name='menu_delete'),
    path('plats/', views.plats_list, name='plats_list'),
    path('plats/create/', views.plats_create, name='plats_create'),
    path('plats/<int:plats_id>/update/', views.plats_update, name='plats_update'),
    path('plats/<int:plats_id>/delete/', views.plats_delete, name='plats_delete'),
]
