from django.db import models

# Create your models here.

class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)

    def price(self):
        sum = 0.0
        for item in self.unit_ingredients.all():
            price = item.ingredient.price()
            if price == 'N/A':
                return 'Price of %s is missing' % item.ingredient.name
            sum += round(price.price / price.quantity * item.quantity_used, 1)
        return '$%s' % str(sum)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    description = models.TextField(null=True)

    def price(self):
        price = self.prices.order_by('-date').first()
        if price is not None:
            return '$%s / %s %s' % (str(price.price), str(price.quantity), self.unit)
        else:
            return 'N/A'

    def __str__(self):
        return self.name

class UnitIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='unit_ingredients', verbose_name='ingredient')
    quantity_used = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    dish = models.ForeignKey(Dish, related_name='unit_ingredients', verbose_name='dish', on_delete=models.CASCADE)

class IngredientPrice(models.Model):
    STATUS_ACTIVE = 'Active'
    STATUS_INACTIVE = 'Inactive'

    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=255)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='prices', verbose_name='ingredient', blank=True, null=True)



