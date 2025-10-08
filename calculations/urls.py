from django.urls import path
from . import views 

urlpatterns = [
    path ('calculations/', views.calculations, name='calculations'),
    path ('create_apartment/', views.create_apartment, name='create_apartment'),
    path ('add_member/', views.add_member, name='add_member'),
    path ('add_bill_share/', views.add_bill_share, name='add_bill_share'),
    path ('apartment_bill_shares/', views.AppartmentBillSharesList.as_view(), name='apartment_bill_shares'),


]