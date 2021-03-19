from django.urls import path
from.import views

urlpatterns = [
    path('login',views.signin,name="login"),
    path('signup',views.signup,name="signup"),
    path('signout',views.signout,name="signout"),

    path('home',views.index,name="home"),

    path('supplier',views.supplier,name="supplier"),
    path('supplier_table/',views.supplier_table,name="supplier_table"),
    path('supplier_table/update/<int:id>',views.supplier_table_update,name="supplier_table_update"),
    path('supplier_table/delete/<int:id>',views.supplier_table_delete,name="supplier_table_delete"),

    path('update_stock',views.update_stock,name="update_stock"),
    path('stock_table/',views.stock_table,name="stock_table"),
    path('stock_table/update/<int:id>',views.stock_table_update,name="stock_table_update"),
    path('stock_table/delete/<int:id>',views.stock_table_delete,name="stock_table_delete"),

    path('product_inward',views.inventory,name="product_inward"),
    path('product_inward_table/',views.inventory_table,name="product_inward_table"),
    path('product_inward_table/update/<int:id>',views.inventory_table_update,name="product_inward_table_update"),
    path('product_inward_table/delete/<int:id>',views.inventory_table_delete,name="product_inward_table_delete"),

    path('product_outward',views.add_product,name="product_outward"),
    path('product_outward_table/',views.product_table,name="product_outward_table"),
    path('product_outward_table/update/<int:id>',views.product_table_update,name="product_outward_table_update"),
    path('product_outward_table/delete/<int:id>',views.product_table_delete,name="product_outward_table_delete"),
    
    path('customer_details',views.customer_details,name="customer_details"),
    path('customer_details_table/',views.customer_details_table,name="customer_details_table"),
    path('customer_details_table/update/<int:id>',views.customer_details_table_update,name="customer_details_table_update"),
    path('customer_details_table/delete/<int:id>',views.customer_details_table_delete,name="customer_details_table_delete"),

    path('invoice',views.billing,name="invoice"),
    path('invoice_table/',views.billing_table,name="invoice_table"),
    path('invoice_table/update/<int:id>',views.billing_table_update,name="invoice_table_update"),
    path('invoice_table/delete/<int:id>',views.billing_table_delete,name="invoice_table_delete"),

]
