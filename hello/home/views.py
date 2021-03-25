from django.shortcuts import render, HttpResponse
from datetime import datetime
from .models import Contact
from .models import Product
from .models import Order
from .models import Order_Update

# Create your views here.

def index(request):
    #return HttpResponse("index home")
    return render(request, 'index.html')

def about(request):
     c = Contact.objects.all()
     context = { 'data' : c}
     return render(request, 'about.html', context)

def services(request):
    return render(request, 'services.html')

def prod_view(request):
    p = Product.objects.all()
    c = {'d': p }
    return render(request, 'allprod.html', c)
def prod_view1(request, s):
    p = Product.objects.filter(name=s)
    context = {
        'pname' : p[0].name,
        'pprice' : p[0].price,
        'pimage' : p[0].image,
        'pdesc' : p[0].desc
    }
    return render(request, 'prod_details.html', context)

def checkout(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        address = request.POST.get('address')
        total_amount = request.POST.get('tam')
        order_id = request.POST.get('order_id')
        o = Order(name=name, email=email, phone=phone, city=city, address=address, total_amount=total_amount, order_id=order_id, date=datetime.today())
        o1 = Order_Update(order_id=order_id, date=datetime.today())
        o.save()
        o1.save()
        print(o)
    return render(request, 'checkout.html')

def tracker(request):
    if request.method == "POST":
        oid = request.POST.get('oid')
        p = Order.objects.filter(order_id=oid)
        p1 = Order_Update.objects.filter(order_id=oid)
        print(p)
        print(len(p))
        if len(p)>0:
            print(p,"hii")
            return render(request, 'tracker.html', { 'oname': p[0], 'odesc' : p1[0]})

    #return render(request, 'tracker.html')
        #c = {'name': p[0].name,'desc': p1[0].desc }
    return render(request, 'tracker.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        query = request.POST.get('query')
        contact = Contact(name=name, email=email, phone=phone, query=query, date=datetime.today())
        contact.save()
        print(contact)
    return render(request, 'contact.html')