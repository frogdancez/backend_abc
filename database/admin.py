from django.contrib import admin
from .models import *

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['CustomerID', 'CustomerName', 'Country', 'Gender', 'Phone', 'PostalCode']
class StoreAdmin(admin.ModelAdmin):
    list_display = ['StoreID', 'Store', 'Region', 'Latitude', 'Longitude']
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['SalesPersonID', 'SalesPersonName', 'Title']
class ProductAdmin(admin.ModelAdmin):
    list_display = ['ProductID', 'Category', 'Product']
class OrderAdmin(admin.ModelAdmin):
    list_display = ['OrdersID', 'SalesDate', 'SalesPerson', 'Customer']
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ['OrderDetailID', 'Order', 'Store', 'Product', 'Quantity', 'Sales']


admin.site.register(Store, StoreAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)