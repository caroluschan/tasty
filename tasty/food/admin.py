from food.models import *
from django.contrib import admin, messages
from jet.admin import CompactInline
from django.utils.html import format_html
from django.shortcuts import redirect
from django.db.models import Count


# Register your models here.

class SourceAdmin(admin.ModelAdmin):
    list_display = ['name', 'latitude', 'longitude']
    list_display_links= ['name', ]
    list_per_page = 10

class IngredientTypeAdmin(admin.ModelAdmin):
    list_display = ['name',]
    list_display_links= ['name', ]
    list_per_page = 10

class ToolTypeAdmin(admin.ModelAdmin):
    list_display = ['name',]
    list_display_links= ['name', ]
    list_per_page = 10

class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'unit','price']
    list_display_links= ['name', ]
    list_per_page = 10

    def price(self, object):
        return object.price()

class ToolAdmin(admin.ModelAdmin):
    list_display = ['name', 'type']
    list_display_links= ['name', ]
    list_per_page = 10

class IngredientInline(admin.TabularInline):
    model = UnitIngredient
    extra = 1
    fields = ['ingredient', 'quantity_used']
    show_change_link = True

class ToolInline(admin.TabularInline):
    model = UnitTool
    extra = 1
    fields = ['tool', 'quantity_used']
    show_change_link = True

class DishAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    list_per_page = 10
    inlines = (IngredientInline, ToolInline, )

    def price(self, object):
        return object.price()


admin.site.register(Source, SourceAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Dish, DishAdmin)
admin.site.register(Tool, ToolAdmin)
admin.site.register(IngredientType, IngredientTypeAdmin)
admin.site.register(ToolType, ToolTypeAdmin)

admin.site.site_header = 'Tasty'
admin.site.site_title = 'Tasty'
admin.site.index_title = 'Admin Console'
admin.site.site_url = None