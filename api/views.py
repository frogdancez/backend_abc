from django.http import JsonResponse
from django.db.models import Sum, Count
from database.models import *
from django.db.models.functions import ExtractYear

# Create your views here.
def index(request):
    data = {
        'status': 1,
        'data': 'Hello, World!'
    }
    return JsonResponse(data)

def getAllYear(request):
    data = {
        'status': 1,
        'data': list(Order.objects.filter().annotate(Year=ExtractYear('SalesDate')).values('Year').distinct())
    }
    return JsonResponse(data)

def getTimeRange(request):
    data = {
        'status': 1,
        'data': list(Order.objects.earliest('SalesDate').SalesDate, Order.objects.latest('SalesDate').SalesDate)
    }
    return JsonResponse(data)

# Overview
def getSales(request, startTime, endTime):
    data = {
        'status': 1,
        'data': list(OrderDetail.objects.filter(Order__SalesDate__range=[startTime, endTime]).values('Order__SalesDate').annotate(Sales=Sum('Sales')))
    }
    return JsonResponse(data)

# Customer
def getCustomerCountrys(request):
    data = {
        'status': 1,
        'data': list(Customer.objects.values('Country').distinct())
    }
    return JsonResponse(data)

def topCustomerBySale(request, startTime, endTime):
    data = {
        'status': 1,
        'data': list(OrderDetail.objects.filter(Order__SalesDate__range=[startTime, endTime]).values('Order__Customer__CustomerName').annotate(Sales=Sum('Sales')).order_by('-Sales'))
    }
    return JsonResponse(data)

def topCustomerByRecord(request, startTime, endTime):
    data = {
        'status': 1,
        'data': list(OrderDetail.objects.filter(Order__SalesDate__range=[startTime, endTime]).values('Order__Customer__CustomerName').annotate(Record=Count('Sales')).order_by('-Record'))
    }
    return JsonResponse(data)

def topCustomerByCountrySale(request, startTime, endTime):
    data = {
        'status': 1,
        'data': list(OrderDetail.objects.filter(Order__SalesDate__range=[startTime, endTime]).values('Order__Customer__Country').annotate(Sales=Sum('Sales')).order_by('-Sales'))
    }
    return JsonResponse(data)

def topCustomerByCountryRecord(request, startTime, endTime):
    data = {
        'status': 1,
        'data': list(OrderDetail.objects.filter(Order__SalesDate__range=[startTime, endTime]).values('Order__Customer__Country').annotate(Record=Count('Sales')).order_by('-Record'))
    }
    return JsonResponse(data)

# Employee
def getEmployees(request):
    data = {
        'status': 1,
        'data': list(Employee.objects.values('SalesPersonName').distinct())
    }
    return JsonResponse(data)

def topEmployeeBySale(request, startTime, endTime):
    data = {
        'status': 1,
        'data': list(OrderDetail.objects.filter(Order__SalesDate__range=[startTime, endTime]).values('Order__SalesPerson__SalesPersonName').annotate(Sales=Sum('Sales')).order_by('-Sales'))
    }
    return JsonResponse(data)

def topEmployeeByRecord(request, startTime, endTime):
    data = {
        'status': 1,
        'data': list(OrderDetail.objects.filter(Order__SalesDate__range=[startTime, endTime]).values('Order__SalesPerson__SalesPersonName').annotate(Record=Count('Sales')).order_by('-Record'))
    }
    return JsonResponse(data)

# Store
def getStores(request):
    data = {
        'status': 1,
        'data': list(Store.objects.values('Store').distinct())
    }
    return JsonResponse(data)

def topStoreBySale(request, startTime, endTime):
    data = {
        'status': 1,
        'data': list(OrderDetail.objects.filter(Order__SalesDate__range=[startTime, endTime]).values('Store__Store', 'Store__Latitude', 'Store__Longitude').annotate(Sales=Sum('Sales')).order_by('-Sales'))
    }
    return JsonResponse(data)

def topStoreByRecord(request, startTime, endTime):
    data = {
        'status': 1,
        'data': list(OrderDetail.objects.filter(Order__SalesDate__range=[startTime, endTime]).values('Store__Store', 'Store__Latitude', 'Store__Longitude').annotate(Record=Count('Sales')).order_by('-Record'))
    }
    return JsonResponse(data)

# product
def getProducts(request):
    data = {
        'status': 1,
        'data': list(Product.objects.values('Product').distinct())
    }
    return JsonResponse(data)

def topProductBySale(request, startTime, endTime):
    data = {
        'status': 1,
        'data': list(OrderDetail.objects.filter(Order__SalesDate__range=[startTime, endTime]).values('Product__Product').annotate(Sales=Sum('Sales')).order_by('-Sales'))
    }
    return JsonResponse(data)

def topProductByRecord(request, startTime, endTime):
    data = {
        'status': 1,
        'data': list(OrderDetail.objects.filter(Order__SalesDate__range=[startTime, endTime]).values('Product__Product').annotate(Record=Count('Sales')).order_by('-Record'))
    }
    return JsonResponse(data)
# category
def getCategories(request):
    data = {
        'status': 1,
        'data': list(Product.objects.values('Category').distinct())
    }
    return JsonResponse(data)

def topCategoryBySale(request, startTime, endTime):
    data = {
        'status': 1,
        'data': list(OrderDetail.objects.filter(Order__SalesDate__range=[startTime, endTime]).values('Product__Category').annotate(Sales=Sum('Sales')).order_by('-Sales'))
    }
    return JsonResponse(data)

def topCategoryByRecord(request, startTime, endTime):
    data = {
        'status': 1,
        'data': list(OrderDetail.objects.filter(Order__SalesDate__range=[startTime, endTime]).values('Product__Category').annotate(Record=Count('Sales')).order_by('-Record'))
    }
    return JsonResponse(data)