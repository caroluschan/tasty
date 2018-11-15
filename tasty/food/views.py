from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from food.forms import *
# Create your views here.

@login_required
def edit_ingredient_price(request):
    print(request.method)
    if request.method == 'POST':
        print('updating ingredient price')
        form = EditIngredientPriceForm(request.POST)
        if form.is_valid():
            price = form.cleaned_data.get('price')
            quantity = form.cleaned_data.get('quantity')
            ingredient = form.cleaned_data.get('ingredient')
            for item in ingredient.prices.all():
                item.status = IngredientPrice.STATUS_INACTIVE
                item.save()
            ingredient_price = IngredientPrice(
                price=price,
                quantity=quantity,
                status=IngredientPrice.STATUS_ACTIVE,
                ingredient=ingredient
            )
            ingredient_price.save()
        return redirect('/admin/edit_ingredient_price')
    else:
        form = EditIngredientPriceForm()
        context = {'form': form, }
        return render(request, 'admin/edit_ingredient_price.html', context)