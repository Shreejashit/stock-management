from django.db import models

# Create your models here.
class add_supplier(models.Model):
    supplier_id = models.CharField(max_length=10)
    supplier_name = models.CharField(max_length=30)
    address = models.CharField(max_length=40)
    cant_no = models.CharField(max_length=10)

    def __str__(self):
        return self.supplier_id + " " + self.supplier_name + " " + self.address + " " + self.cant_no

class stock_updating(models.Model):
    product_name = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    inner_quantity = models.CharField(max_length=10)
    outer_quantity = models.CharField(max_length=10)    

    def __str__(self):
        return self.product_name+" "+self.category+" "+self.inner_quantity+" "+self.outer_quantity

class product_inward(models.Model):
    product_id = models.CharField(max_length=10)
    product_name = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    brand_name = models.CharField(max_length=30)

    def __str__(self):
        return self.product_id+" "+self.product_name+" "+self.category+" "+self.brand_name

class product_outward(models.Model):
    product_id = models.CharField(max_length=10)
    product_name = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    quantity = models.CharField(max_length=10)

    def __str__(self):
        return self.product_id+" "+self.product_name+" "+self.category+" "+self.quantity

class customer_details(models.Model):
    customer_id = models.CharField(max_length=10)
    customer_name = models.CharField(max_length=20)
    address = models.CharField(max_length=40)
    cant_no = models.CharField(max_length=10)

    def __str__(self):
        return self.customer_id+" "+self.customer_name+" "+self.address+" "+self.cant_no

class billing(models.Model):
    invoice_id = models.CharField(max_length=10)
    product_id = models.CharField(max_length=10)
    product_name = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    quantity = models.CharField(max_length=10)
    
    def __str__(self):
        return self.product_id+" "+self.product_name+" "+self.category+" "+self.quantity+" "+self.invoice_id

