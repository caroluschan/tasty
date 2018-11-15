from django.db import models
import decimal
# Create your models here.

class Source(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=12, decimal_places=8)
    longitude = models.DecimalField(max_digits=12, decimal_places=8)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def price(self):
        sum = decimal.Decimal(0.0)
        for item in self.unit_ingredients.all():
            price = item.ingredient.latestIngredientPrice()
            if price == None:
                return 'Price of %s is missing' % item.ingredient.name
            sum = sum + round(price.price / price.quantity * item.quantity_used, 1)
        return '$%s' % str(sum)

    def __str__(self):
        return self.name

class IngredientType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ToolType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Tool(models.Model):
    name = models.CharField(max_length=255)
    unit = models.CharField(max_length=255, blank=True, null=True)
    type = models.ForeignKey(ToolType, on_delete=models.CASCADE, related_name='tools', verbose_name='type', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    sources = models.ManyToManyField(Source, blank=True, null=True)

    def __str__(self):
        return self.name + '-' + self.type.name

class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    type = models.ForeignKey(IngredientType, on_delete=models.CASCADE, related_name='ingredients', verbose_name='type', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    sources = models.ManyToManyField(Source, blank=True, null=True)

    def price(self):
        price = self.prices.order_by('-date').first()
        if price is not None:
            return '$%s / %s %s' % (str(price.price), str(price.quantity), self.unit)
        else:
            return 'N/A'
    def latestIngredientPrice(self):
         return self.prices.order_by('-date').first()

    def __str__(self):
        return self.name + '-' + self.type.name

class UnitIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='unit_ingredients', verbose_name='ingredient')
    quantity_used = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    dish = models.ForeignKey(Dish, related_name='unit_ingredients', verbose_name='dish', on_delete=models.CASCADE)

class UnitTool(models.Model):
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE, related_name='unit_tools', verbose_name='tool')
    quantity_used = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    dish = models.ForeignKey(Dish, related_name='unit_tools', verbose_name='dish', on_delete=models.CASCADE)

class IngredientPrice(models.Model):
    STATUS_ACTIVE = 'Active'
    STATUS_INACTIVE = 'Inactive'

    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=255)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='prices', verbose_name='ingredient', blank=True, null=True)
    source = models.ForeignKey(Source, on_delete=models.CASCADE, related_name='prices', verbose_name='source', blank=True, null=True)




