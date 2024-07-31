"""
URL configuration for pro project.

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
from django.urls import path
from app1 import views
from django.conf.urls.static import static
from django.conf import settings 


urlpatterns = [
    path('admin/', admin.site.urls),
       path('', views.index, name="index"),
        path('about/', views.about, name="about"),
        path('product_list/', views.product_list, name="product_list"),
        path('single_product/', views.single_product, name="single_product"),
        path('blog/', views.blog, name="blog"),
        path('single_blog/', views.single_blog, name="single_blog"),
        path('login/', views.login, name="login"),
        path('contact/', views.login, name="contact"),
        path('checkout/', views.checkout, name="checkout"),
        path('cart/', views.cart, name="cart"),
        path('add_to_cart/<int:id>', views.add_to_cart, name="add_to_cart"),
        path('start_order/', views.start_order, name='start_order'),
        path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
        path('confirmation/', views.confirmation, name="confirmation"),
        path('elements/', views.elements, name="elements"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

