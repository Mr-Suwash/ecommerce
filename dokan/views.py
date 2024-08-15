from django.shortcuts import render

# Create your views here.
from .models import product

def index(request):
    product_object= product.objects.all()
    return render(request, 'dokan/index.html', {'product_object':product_object } )