from django.contrib import admin
from .models import *

# Register your models here.

class CustomersAdmin(admin.ModelAdmin):
    list_display = ['CustomerID', 'CustomerName', 'Country', 'Gender', 'Phone', 'PostalCode']
class StoresAdmin(admin.ModelAdmin):
    list_display = ['StoreID', 'Store', 'Region', 'Latitude', 'Longitude']
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ['SalesPersonID', 'SalesPersonName', 'Title']
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['ProductID', 'Category', 'Product']
class OrdersAdmin(admin.ModelAdmin):
    list_display = ['OrdersID', 'SalesDate', 'SalesPerson', 'Customer']
class OrderDetailsAdmin(admin.ModelAdmin):
    list_display = ['OrderDetailID', 'Order', 'Store', 'Product', 'Quantity', 'Sales']


admin.site.register(Stores, StoresAdmin)
admin.site.register(Customers, CustomersAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Employees, EmployeesAdmin)
admin.site.register(Orders, OrdersAdmin)
admin.site.register(OrderDetails, OrderDetailsAdmin)