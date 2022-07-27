from django.urls import path
from api.views import *

urlpatterns = [
    path('', index, name='index'),
    # intelligence
    # front-end
    path('getAllYear', getAllYear, name='getAllYear'),
    path('getTimeRange', getTimeRange, name='getTimeRange'),
    # overview
    path('getSales/<str:startTime>/<str:endTime>', getSales, name='getSales'),
    # customer
    path('topCustomerBySale', topCustomerBySale, name='topCustomerBySale'),
    path('topCustomerByRecord', topCustomerByRecord, name='topCustomerByRecord'),
    path('topCustomerByCountrySale', topCustomerByCountrySale, name='topCustomerByCountrySale'),
    path('topCustomerByCountryRecord', topCustomerByCountryRecord, name='topCustomerByCountryRecord'),
    # employee
    path('topEmployeeBySale', topEmployeeBySale, name='topEmployeeBySale'),
    path('topEmployeeByRecord', topEmployeeByRecord, name='topEmployeeByRecord'),
    # store
    path('topStoreByRecord', topStoreByRecord, name='topStoreByRecord'),
    path('topStoreBySale', topStoreBySale, name='topStoreBySale'),
]