from django.http import JsonResponse
from django.db.models import Sum
from database.models import *

# Create your views here.
def index(request):
    data = {
        'status': 1,
        'data': 'Hello, World!'
    }
    return JsonResponse(data)

# Overview
def getSales(request):
    data = {
        'status': 1,
        'data': list(OrderDetail.objects.values('Order__SalesDate').annotate(Sales=Sum('Sales')))
    }
    return JsonResponse(data)

# Customer
def top10Customer(request):
    data = {
        'status': 1,
        'data': list(OrderDetail.objects.values('Order__Customer__CustomerName').annotate(Sales=Sum('Sales')).order_by('-Sales'))
    }
    return JsonResponse(data)


