from django.shortcuts import render,redirect
from django.forms import ModelForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .import views
from . import models
from django.db import IntegrityError

def signin(request):
    alert = False
    if request.method=='POST':

        username= request.POST['username']
        password= request.POST['password']
        
        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return render(request, "index.html",{'alert':True})
        else:
            return render(request, "login.html",{'alert':False})
            

    return render(request, "login.html",{'alert':alert})

def signup(request):
    alert = False
    try:
        if request.method=='POST':
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            user = User.objects.create_user(username = username,password=password,email= email)
            user.save()
            alert = "User created"
            return redirect('login')
    except IntegrityError as e:
        print(e)
        alert = "User already Exist"
        return render(request,"signup.html",{'alert':alert})

    return render(request,"signup.html",{'alert':alert})

def signout(request):
    return redirect('login')

def index(request):
    return render(request, "index.html",{})

class SupplierDetails(ModelForm):
    class Meta:
        model = models.add_supplier
        fields = '__all__'

def supplier(request):
    alert = False
    form1 = SupplierDetails(request.POST)
    if request.method=='POST':
        if form1.is_valid():
            form1.save()
            alert = "Supplier Details Updated Successfully"
        return render(request,"supplier.html",{'sr':form1,'alert': alert})
    else:
        return render(request,"supplier.html",{'sr':form1,'alert':False}) 
    return render(request,"supplier.html",{'sr':form1,'alert':alert})

def supplier_table(request):
    db = models.add_supplier.objects.all()
    return render(request,"supplier_table.html",{'db':db})    

def supplier_table_update(request,id):
    db = models.add_supplier.objects.get(id=id)
    form1 = SupplierDetails(request.POST,instance = db)
    if request.method=='POST':
        if form1.is_valid():
            db.supplier_id = form1.cleaned_data['supplier_id']
            db.supplier_name = form1.cleaned_data['supplier_name']
            db.address = form1.cleaned_data['address']
            db.cant_no = form1.cleaned_data['cant_no']
            db.save()
    return render(request,"supplier.html",{'sr':form1})

def supplier_table_delete(request,id):
    db = models.add_supplier.objects.get(id=id)
    db.delete()
    db = models.add_supplier.objects.all()
    return redirect('supplier_table')


class Updating_stock(ModelForm):
    class Meta:
        model = models.stock_updating
        fields = '__all__'

def update_stock(request):
    alert = False
    form2 = Updating_stock(request.POST)
    if request.method == 'POST':
        if form2.is_valid():
            form2.save()
        return render(request, "update_stock.html",{'us':form2,'alert':"Stocks Updated Successfully"})    
    else:
        return render(request, "update_stock.html",{'us':form2,'alert':False})
    return render(request, "update_stock.html",{'us':form2,'alert':alert})

def stock_table(request):
    db = models.stock_updating.objects.all()
    return render(request,"stock_table.html",{'db':db})

def stock_table_update(request,id):
    db = models.stock_updating.objects.get(id=id)
    form2 = Updating_stock(request.POST,instance = db)
    if request.method=='POST':
        if form2.is_valid():
            db.product_name = form2.cleaned_data['product_name']
            db.category = form2.cleaned_data['category']
            db.inner_quantity = form2.cleaned_data['inner_quantity']
            db.outer_quantity = form2.cleaned_data['outer_quantity']
            db.save()
    return render(request,"update_stock.html",{'us':form2})

def stock_table_delete(request,id):
    db = models.stock_updating.objects.get(id=id)
    db.delete()
    db = models.stock_updating.objects.all()
    return redirect('stock_table')

class Inventory(ModelForm):
    class Meta:
        model = models.product_inward
        fields = '__all__'

def inventory(request):
    alert = False
    form3 = Inventory(request.POST)
    if request.method=='POST':
        if form3.is_valid():
            form3.save()
        return render(request, "inventory.html",{'iv':form3,'alert':"Inventory Updated Successfully"})    
    else:
        return render(request, "inventory.html",{'iv':form3,'alert':False})
    return render(request, "inventory.html",{'iv':form3,'alert':alert})

def inventory_table(request):
    db = models.product_inward.objects.all()
    return render(request,"inventory_table.html",{'db':db})

def inventory_table_update(request,id):
    db = models.product_inward.objects.get(id=id)
    form3 = Inventory(request.POST,instance = db)
    if request.method=='POST':
        if form3.is_valid():
            db.product_id = form3.cleaned_data['product_id']
            db.product_name = form3.cleaned_data['product_name']
            db.category = form3.cleaned_data['category']
            db.brand_name = form3.cleaned_data['brand_name']
            db.save()
    return render(request,"inventory.html",{'iv':form3})

def inventory_table_delete(request,id):
    db = models.product_inward.objects.get(id=id)
    db.delete()
    db = models.product_inward.objects.all()
    return redirect('product_inward_table')

class AddProduct(ModelForm):
    class Meta:
        model=models.product_outward
        fields = '__all__'

def add_product(request):
    alert = False
    form4 = AddProduct(request.POST)
    if request.method=='POST':
        if form4.is_valid():
            form4.save()
            alert = "Products Added Successfully"
        return render(request,"products.html",{'pd':form4,'alert': alert})
    else:
        return render(request,"products.html",{'pd':form4,'alert':False}) 
    return render(request,"products.html",{'pd':form4,'alert':alert})

def product_table(request):
    db = models.product_outward.objects.all()
    return render(request,"products_table.html",{'db':db})

def product_table_update(request,id):
    db = models.product_outward.objects.get(id=id)
    form4 = AddProduct(request.POST,instance = db)
    if request.method=='POST':
        if form4.is_valid():
            db.product_id = form4.cleaned_data['product_id']
            db.product_name = form4.cleaned_data['product_name']
            db.category = form4.cleaned_data['category']
            db.quantity = form4.cleaned_data['quantity']
            db.save()
    return render(request,"products.html",{'pd':form4})

def product_table_delete(request,id):
    db = models.product_outward.objects.get(id=id)
    db.delete()
    db = models.product_outward.objects.all()
    return redirect('product_outward_table')


class CustomerDetails(ModelForm):
    class Meta:
        model = models.customer_details
        fields = '__all__'

def customer_details(request):
    alert = False
    form5 = CustomerDetails(request.POST)
    if request.method=='POST':
        if form5.is_valid():
            form5.save()
            alert = "Customer Details Updated Successfully"
        return render(request, "customer_details.html",{'cd':form5,'alert':alert})
    else:
        return render(request, "customer_details.html",{'cd':form5,'alert':False})
    return render(request, "customer_details.html",{'cd':form5,'alert':alert})

def customer_details_table(request):
    db = models.customer_details.objects.all()
    return render(request,"customer_details_table.html",{'db':db})

def customer_details_table_update(request,id):
    db = models.customer_details.objects.get(id=id)
    form5 = CustomerDetails(request.POST,instance = db)
    if request.method=='POST':
        if form5.is_valid():
            db.customer_id = form5.cleaned_data['customer_id']
            db.customer_name = form5.cleaned_data['customer_name']
            db.address = form5.cleaned_data['address']
            db.cant_no = form5.cleaned_data['cant_no']
            db.save()
    return render(request,"customer_details.html",{'cd':form5})

def customer_details_table_delete(request,id):
    db = models.customer_details.objects.get(id=id)
    db.delete()
    db = models.customer_details.objects.all()
    return redirect('customer_details_table')

class Invoice(ModelForm):
    class Meta:
        model=models.billing
        fields = '__all__'

def billing(request):
    alert = False
    form6 = Invoice(request.POST)
    if request.method=='POST':
        if form6.is_valid():
            form6.save()
            alert = "Billing Completed Successfully"
        return render(request, "invoice.html",{'bg':form6,'alert':alert})
    else:
        return render(request, "invoice.html",{'bg':form6,'alert':False})    
    return render(request, "invoice.html",{'bg':form6,'alert':alert})

def billing_table(request):
    db = models.billing.objects.all()
    return render(request,"invoice_table.html",{'db':db})

def billing_table_update(request,id):
    db = models.billing.objects.get(id=id)
    form6 = Invoice(request.POST,instance = db)
    if request.method=='POST':
        if form6.is_valid():
            db.invoice_id = form6.cleaned_data['invoice_id']
            db.product_id = form6.cleaned_data['product_id']
            db.product_name = form6.cleaned_data['product_name']
            db.category = form6.cleaned_data['category']
            db.quantity = form6.cleaned_data['quantity']
            db.save()
    return render(request,"invoice.html",{'bg':form6})

def billing_table_delete(request,id):
    db = models.billing.objects.get(id=id)
    db.delete()
    db = models.billing.objects.all()
    return redirect('invoice_table')

