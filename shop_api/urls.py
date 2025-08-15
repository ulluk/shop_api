"""
URL configuration for shop_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from product.views import (category_list_create_api_view, category_detail_api_view , product_detail_api_view, 
                           product_list_create_api_view, review_detail_api_view,review_list_api_view, review_of_product_api_view,)
from users.views import (registration_api_view, authorization_api_view, confirmation_api_view)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/categories', category_list_create_api_view),
    path('api/v1/categories/<int:id>', category_detail_api_view),
    path('api/v1/products', product_list_create_api_view),
    path('api/v1/products/<int:id>', product_detail_api_view),
    path('api/v1/reviews', review_list_api_view),
    path('api/v1/reviews/<int:id>', review_detail_api_view),
    path('api/v1/products/reviews', review_of_product_api_view),
    path('api/v1/users/registration/', registration_api_view),
    path('api/v1/users/authorization/', authorization_api_view),
    path('api/v1/users/confirm/', confirmation_api_view)
]
