from django.contrib import admin
from Recipes.models import Profile, Recipe, RecipeIngredient

admin.site.register(Profile)
admin.site.register(Recipe)
admin.site.register(RecipeIngredient)

