from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Home"),
    path('contact/', views.contact, name="Contact"),
    path('contact-submit/', views.contactSubmit, name="Submit"),
    path('products/', views.productListingPage, name="Products"),
    path('about/', views.about, name="About"),
    path('product_details/<int:primary_key>', views.product_details, name="Product Details"),
]