from django.urls import path
from api.views import *

urlpatterns = [
    path('', index, name='index'),
    # intelligence
    # static
    path('singPath', singPath, name='singPath'),
    path('worldPath', worldPath, name='worldPath'),
    # overview
    path('getSales', getSales, name='getSales'),
    # customer
    path('topCustomerBySale', topCustomerBySale, name='topCustomerBySale'),
    path('topCustomerByRecord', topCustomerByRecord, name='topCustomerByRecord'),
    path('topCustomerByCountrySale', topCustomerByCountrySale, name='topCustomerByCountrySale'),
    path('topCustomerByCountryRecord', topCustomerByCountryRecord, name='topCustomerByCountryRecord'),
    # employee
    path('topEmployeeBySale', topEmployeeBySale, name='topEmployeeBySale'),
    path('topEmployeeByRecord', topEmployeeByRecord, name='topEmployeeByRecord'),
    # store
    path('topEmployeeByRecord', topEmployeeByRecord, name='topEmployeeByRecord'),
    path('topEmployeeBySale', topEmployeeBySale, name='topEmployeeBySale'),
]