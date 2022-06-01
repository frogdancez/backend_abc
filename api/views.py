from django.http import HttpResponse, JsonResponse
from django.db.models import Sum, Count
from database.models import *

# Create your views here.
def index(request):
    data = {
        'status': 1,
        'data': 'Hello, World!'
    }
    return JsonResponse(data)

# static file
def singPath(request):
    return HttpResponse(open('.\api\static\singapore.geojson', "r"))

def worldPath(request):
    return HttpResponse(open('.\api\static\world.geojson', "r"))

# Overview
def getSales(request):
    data = {
        'status': 1,
        'data': list(OrderDetail.objects.values('Order__SalesDate').annotate(Sales=Sum('Sales')))
    }
    return JsonResponse(data)

# Customer
def topCustomerBySale(request):
    data = {
        'status': 1,
        'data': list(OrderDetail.objects.values('Order__Customer__CustomerName').annotate(Sales=Sum('Sales')).order_by('-Sales'))
    }
    return JsonResponse(data)

def topCustomerByRecord(request):
    data = {
        'status': 1,
        'data': list(OrderDetail.objects.values('Order__Customer__CustomerName').annotate(Record=Count('Sales')).order_by('-Record'))
    }
    return JsonResponse(data)

def topCustomerByCountrySale(request):
    data = {
        'status': 1,
        'data': list(OrderDetail.objects.values('Order__Customer__Country').annotate(Sales=Sum('Sales')).order_by('-Sales'))
    }
    return JsonResponse(data)

def topCustomerByCountryRecord(request):
    data = {
        'status': 1,
        'data': list(OrderDetail.objects.values('Order__Customer__Country').annotate(Record=Count('Sales')).order_by('-Record'))
    }
    return JsonResponse(data)

# Employee
def topEmployeeBySale(request):
    data = {
        'status': 1,
        'data': list(OrderDetail.objects.values('Order__SalesPerson__SalesPersonName').annotate(Sales=Sum('Sales')).order_by('-Sales'))
    }
    return JsonResponse(data)

def topEmployeeByRecord(request):
    data = {
        'status': 1,
        'data': list(OrderDetail.objects.values('Order__SalesPerson__SalesPersonName').annotate(Record=Count('Sales')).order_by('-Record'))
    }
    return JsonResponse(data)

# Store
def topStoreBySale(request):
    data = {
        'status': 1,
        'data': list(OrderDetail.objects.values('Store__Store').annotate(Sales=Sum('Sales')).order_by('-Sales'))
    }
    return JsonResponse(data)

def topStoreByRecord(request):
    data = {
        'status': 1,
        'data': list(OrderDetail.objects.values('Store__Store').annotate(Record=Count('Sales')).order_by('-Record'))
    }
    return JsonResponse(data)
