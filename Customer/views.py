from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Customer
# Create your views here.

# views.py
from django.shortcuts import render, redirect
from .models import Customer

def add_customer(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone_number')
        email = request.POST.get('email')

        Customer.objects.create(
            name=name,
            phone_number=phone,
            email=email
        )
        return redirect('customer_list')

    
    if request.method == "DELETE":
        Customer.delete()
    return render(request, 'add_customer.html')

def update_customer(request, id):
    customer = get_object_or_404(Customer, id=id)

    if request.method == 'POST':
        customer.name = request.POST.get('name')
        customer.phone_number = request.POST.get('phone_number')
        customer.email = request.POST.get('email')
        customer.save()
        return redirect('customer_list')

    context = {'customer': customer}
    return render(request, 'update_customer.html', context)


def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})
