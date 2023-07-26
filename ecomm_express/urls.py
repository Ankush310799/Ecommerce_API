"""
URL configuration for ecomm_express project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import include
from django.urls import re_path
from rest_framework.authtoken import views
from owner.views import CustomUserLoginView ,CustomUserLogoutView
from product.views import ProductListAPIViewSet
from customer.views import CartProductsListAPIViewSet,BuyProductsListAPIViewSet


from ecomm_express.routers import router

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path('api/', include(router.urls)),
    re_path('api-auth/', include('rest_framework.urls')),
    re_path('custom/login/', CustomUserLoginView.as_view(), name='my_custom_login'),
    re_path('api/logout/', CustomUserLogoutView.as_view(), name="logout"),
    re_path('api-token-auth/', views.obtain_auth_token),
    re_path('productlist/', ProductListAPIViewSet.as_view(), name='product_list'),
    re_path('cart/',CartProductsListAPIViewSet.as_view(), name='cart'),
    re_path('buy/',BuyProductsListAPIViewSet.as_view(), name='buy_product'),
    #re_path('auth_user_productlist/', AuthUserProductListAPIViewSet.as_view(), name='auth_user_product_list'),
]
