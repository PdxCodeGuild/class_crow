from django.contrib import admin

# Register your models here.
from .models import Food, Ingredient

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name',)

class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating')

admin.site.register(Food, FoodAdmin)
admin.site.register(Ingredient, IngredientAdmin)