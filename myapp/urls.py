# urls.py
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Home, name='home-page'),
    path('about/', About, name='about-page'),
    path('contact/', Contact, name='contact-page'),
    path('apple/', Apple, name='apple-page'),
    path('addproduct/', AddProduct, name='addproduct-page'),
    path('allproduct/', Product, name='allproduct-page'),
    path('register/',Register, name='register-page'), #localhost:8000/register
    path('addtocart/<int:pid>/',AddtoCart,name='addtocart-page'),
    path('mycart/',MyCart,name='mycart-page'),
    path('mycart/edit/',MyCartEdit,name='mycartedit-page'),
    path('checkout/',Checkout,name='checkout-page'),
    path('orderlist/',OrderListPage, name='orderlist-page'),
    path('allorderlist/',AllOrderListPage, name='allorderlist-page'),
    path('uploadslip/<str:orderid>/',UploadSlip,name='uploadslip-page'),
    path('updatestatus/<str:orderid>/<str:status>/', UpdatePaid, name='updatestatus'),
    path('updatetracking/<str:orderid>/',UpdateTracking,name='updatetracking'),
    path('myorder/<str:orderid>/',MyOrder, name='myorder-page')
]