from django.contrib import admin
from .models import User, Menu, Plats, Commandes, OrderItem, Reservation, Payment

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_number', 'is_customer', 'is_staff', 'is_admin', 'date_joined')
    search_fields = ('username', 'email', 'phone_number')
    list_filter = ('is_customer', 'is_staff', 'is_admin', 'date_joined')
    ordering = ('-date_joined',)

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name', 'description')
    ordering = ('-created_at',)

@admin.register(Plats)
class PlatsAdmin(admin.ModelAdmin):
    list_display = ('name', 'menu', 'price', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('menu', 'created_at')
    ordering = ('-created_at',)

@admin.register(Commandes)
class CommandesAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_amount', 'status', 'created_at')
    search_fields = ('user__username', 'status')
    list_filter = ('status', 'created_at')
    ordering = ('-created_at',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'dish', 'quantity', 'subtotal')
    search_fields = ('order__id', 'dish__name')
    ordering = ('order',)

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'time', 'num_guests', 'created_at')
    search_fields = ('user__username', 'special_requests')
    list_filter = ('date', 'created_at')
    ordering = ('-created_at',)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'Commandes', 'amount', 'method', 'status', 'created_at')
    search_fields = ('Commandes__id', 'method', 'status')
    list_filter = ('method', 'status', 'created_at')
    ordering = ('-created_at',)
