"""Shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

app_name = 'Physical'
from django.contrib import admin
from django.urls import path
from Physical import urls
from Physical import views
urlpatterns = [
    path('',views.dashboard, name="dashboard"),
    path('create_product/',views.ProductCreateView.as_view(), name="productcreateview"),
    path('update_product/',views.updatestock, name="productupdateview"),
    path('sellstock/',views.sellstock, name="sellstock"),
    path('cart_detail', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/',views.cart_add,name='cart_add'),
    path('remove/<int:product_id>/',views.cart_remove,name='cart_remove'),
    path('sales/',views.sale_done,name= 'sale_done'),
]