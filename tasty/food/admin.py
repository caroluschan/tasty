from food.models import *
from django.contrib import admin, messages
from jet.admin import CompactInline
from django.utils.html import format_html
from django.shortcuts import redirect
from django.db.models import Count


# Register your models here.

class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name', 'unit','price']
    list_display_links= ['name', ]
    list_per_page = 10

    def price(self, object):
        return object.price()

class IngredientInline(admin.TabularInline):
    model = UnitIngredient
    extra = 1
    fields = ['ingredient', 'quantity_used']
    show_change_link = True

class DishAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    list_per_page = 10
    inlines = (IngredientInline,)

    def price(self, object):
        return object.price()








admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Dish, DishAdmin)

admin.site.site_header = 'Tasty'
admin.site.site_title = 'Tasty'
admin.site.index_title = 'Admin Console'
admin.site.site_url = None