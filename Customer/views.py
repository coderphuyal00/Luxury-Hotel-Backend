from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Customer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

# views.py
from django.shortcuts import render, redirect
from .models import Customer

@csrf_exempt
def add_customer(request):
    if request.method == 'POST':
        import json
        data = json.loads(request.body.decode('utf-8'))

        name = data.get('name')
        phone = data.get('phone_number')
        email = data.get('email')
        Customer.objects.update_or_create(
            name=name,
            phone_number=phone,
            email=email
        )
        return redirect('/')

    
    if request.method == "DELETE":
        Customer.delete()

    return HttpResponse("added successfully ")
    # return render(request, 'add_customer.html')

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
    data=list(customers.values())
    # return render(request, 'customer_list.html', {'customers': customers})
    return JsonResponse(data,safe=False)
