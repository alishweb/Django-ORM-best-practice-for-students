from django.shortcuts import render
from django.db.models import Q

from .models import Product, Order, OrderItem

# 1- select all products from the database
# def store_view(request):
#     products_queryset = Product.objects.all()
#     print(products_queryset)
#     return render(request, 'store/store.html')

# def store_view(request):
#     # queryset = Product.objects.values('id', 'name', 'unit_price')
#     queryset = Product.objects.only('id', 'name', 'unit_price')
#     print(queryset)
#     return render(request, 'store/store.html')


# 2- select a specific product from the database
# def store_view(request):
#     products = Product.objects.get(id=1)
#     print(products)
#     return render(request, 'store/store.html')

# 3- select all products with inventory less than 10
# def store_view(request):
#     products = Product.objects.filter(inventory__lt=10)
#     print(products)
#     return render(request, 'store/store.html')

# 4- select all products with name contains 'Information'
# def store_view(request):
#     products = Product.objects.filter(name__contains='Information')
#     print(products)
#     return render(request, 'store/store.html')

# 5- select all products with name contains 'site' and inventory greater than 15 and created in 2024
# def store_view(request):
#     queryset = Product.objects.filter(name__icontains='site').filter(datetime_created__year=2024).filter(inventory__gt=15)
#     print(queryset)
#     return render(request, 'store/store.html')

# 6- select all orders with status 'Unpaid'
# def store_view(request):
#     queryset = Order.objects.filter(status='U')
#     print(queryset)
#     return render(request, 'store/store.html')

# 7- select all orders with customer name contains 'John'
# def store_view(request):
#     queryset = OrderItem.objects.filter(order__customer__first_name__icontains='Terri')
#     print(queryset)
#     return render(request, 'store/store.html')


# 8- select all products with inventory less than 5 or greater than 95
# def store_view(request):
#     queryset = Product.objects.filter(Q(inventory__lt=5) | Q(inventory__gt=95))
#     print(queryset)
#     return render(request, 'store/store.html')


# 9- select all products with inventory greater than 90 and order by unit price
# def store_view(request):
#     queryset = Product.objects.filter(inventory__gt=90).order_by('unit_price')
#     print(queryset)
#     return render(request, 'store/store.html')


# 10- diffrent between select_related query and without select_related
# def store_view(request):
#     queryset = OrderItem.objects.all()
#     return render(request, 'store/store.html', {'orderitems': queryset})

# def store_view(request):
#     queryset = OrderItem.objects.select_related('order').all()
#     return render(request, 'store/store.html', {'orderitems': queryset})

#----------------------------------------------------------------------------

# 11- diffrent between prefetch_related query and without prefetch_related
def store_view(request):
    queryset = Product.objects.all()
    return render(request, 'store/store.html', {'products': queryset})


def store_view(request):
    queryset = Product.objects.prefetch_related('comments').all()
    return render(request, 'store/store.html', {'products': queryset})
