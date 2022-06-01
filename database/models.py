from django.db import models

# Create your models here.
class Customer(models.Model):
    CustomerID = models.AutoField(primary_key=True)
    Country = models.CharField(max_length=15)
    CustomerName = models.CharField(max_length=40)
    Gender = models.CharField(max_length=10)
    Phone = models.CharField(max_length=20)
    PostalCode = models.CharField(max_length=15)

    def __str__(self):
        return self.CustomerName

class Employee(models.Model):
    SalesPersonID = models.AutoField(primary_key=True)
    SalesPersonName = models.CharField(max_length=40)
    Title = models.CharField(max_length=25)

    def __str__(self):
        return self.SalesPersonName

class Product(models.Model):
    ProductID = models.AutoField(primary_key=True)
    Category = models.CharField(max_length=40)
    Product = models.CharField(max_length=40)

    def __str__(self):
        return self.Product

class Store(models.Model):
    StoreID = models.AutoField(primary_key=True)
    Region = models.CharField(max_length=10)
    Store = models.CharField(max_length=40)
    Latitude = 	models.FloatField()
    Longitude = models.FloatField()

    def __str__(self):
        return self.Store

class Order(models.Model):
    OrdersID = models.AutoField(primary_key=True)
    SalesDate = models.DateField()
    SalesPerson = models.ForeignKey(Employee, on_delete=models.CASCADE)
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.OrdersID)

class OrderDetail(models.Model):
    OrderDetailID = models.AutoField(primary_key=True)
    Order = models.ForeignKey(Order, on_delete=models.CASCADE)
    Store = models.ForeignKey(Store, on_delete=models.CASCADE)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Quantity = models.PositiveSmallIntegerField()
    Sales = models.FloatField()

    def __str__(self):
        return str(self.OrderDetailID)
