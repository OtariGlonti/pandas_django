from django.shortcuts import render
from .models import Product, Purchase
import pandas as pd

# Create your views here.
def chart_select_view(request):
    product_df = pd.DataFrame(Product.objects.all().values())
    purchase_df = pd.DataFrame(Purchase.objects.all().values())
    #print(product_df)
    context = {
        'products': product_df.to_html,  # in the template the key will be used
        'purchase': purchase_df.to_html,
    }
    return render(request, 'products/main.html', context)
"""
def chart_select_view(request):
    
    qs = Product.objects.all() # get all saved products from the db
    qs1 = Product.objects.all().values() # returns dictionary with many details
    qs2 = Product.objects.all().values_list() # returns tuples? with less details
    print(qs1)
    print("-----------")
    print(qs2)
    return render(request, 'products/main.html',{})  #{} empty dictionary
"""