from django.urls import path
from .views import show_products
urlpatterns = [
    path('product/',view=show_products, name= "Product")
]
