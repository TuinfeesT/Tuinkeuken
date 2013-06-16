from django.contrib import admin

from .models import Ingredient, Ingredients, Recipe

admin.site.register(Ingredient)
admin.site.register(Ingredients)
admin.site.register(Recipe)
