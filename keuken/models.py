from django.db import models
from django.contrib.auth.models import User


class Ingredient(models.Model):
    quantity = models.DecimalField(decimal_places=2, max_digits=6)
    unit = models.CharField(max_length=32, blank=True)
    name = models.CharField(max_length=32, blank=False)
    origin = models.ForeignKey('Ingredients')

    def __str__(self):
        return '{}{} {}'.format(self.quantity, self.unit, self.name)


class Ingredients(models.Model):
    name = models.CharField(max_length=256, blank=True)
    note = models.TextField(blank=True)
    recipe = models.ForeignKey('Recipe', blank=False)

    def __str__(self):
        return '{} ({})'.format(self.name or 'Ingredients', self.recipe)


class Recipe(models.Model):
    name = models.CharField(max_length=256, blank=False)
    author = models.ForeignKey(User)
    pub_date = models.DateField(auto_now_add=True)
    # a free form text field containing the cooking directions
    directions = models.TextField(blank=False)

    def __str__(self):
        return self.name
