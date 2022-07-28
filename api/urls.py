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
    path('getCustomerCountrys', getCustomerCountrys, name='getCustomerCountrys'),
    path('topCustomerBySale/<str:startTime>/<str:endTime>', topCustomerBySale, name='topCustomerBySale'),
    path('topCustomerByRecord/<str:startTime>/<str:endTime>', topCustomerByRecord, name='topCustomerByRecord'),
    path('topCustomerByCountrySale/<str:startTime>/<str:endTime>', topCustomerByCountrySale, name='topCustomerByCountrySale'),
    path('topCustomerByCountryRecord/<str:startTime>/<str:endTime>', topCustomerByCountryRecord, name='topCustomerByCountryRecord'),
    # employee
    path('getEmployees', getEmployees, name='getEmployees'),
    path('topEmployeeBySale/<str:startTime>/<str:endTime>', topEmployeeBySale, name='topEmployeeBySale'),
    path('topEmployeeByRecord/<str:startTime>/<str:endTime>', topEmployeeByRecord, name='topEmployeeByRecord'),
    # store
    path('getStores', getStores, name='getStores'),
    path('topStoreByRecord/<str:startTime>/<str:endTime>', topStoreByRecord, name='topStoreByRecord'),
    path('topStoreBySale/<str:startTime>/<str:endTime>', topStoreBySale, name='topStoreBySale'),
    # product
    path('getProducts', getProducts, name='getProducts'),
    path('topProductBySale/<str:startTime>/<str:endTime>', topProductBySale, name='topProductBySale'),
    path('topProductByRecord/<str:startTime>/<str:endTime>', topProductByRecord, name='topStoreBySale'),
    # category
    path('getCategories', getCategories, name='getCategories'),
    path('topCategoryBySale/<str:startTime>/<str:endTime>', topCategoryBySale, name='topCategoryBySale'),
    path('topCategoryByRecord/<str:startTime>/<str:endTime>', topCategoryByRecord, name='topCategoryByRecord'),
]