from django.contrib import admin
from django.urls import path
from .views import ProductViewSet, UserViewSet
urlpatterns = [
    path('products', ProductViewSet.as_view({
        'get': 'list',
        'post': 'create',

    })),

    path('products/<str:pk>', ProductViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',

    })),

    path('user', UserViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),

    path( 'user/<str:pk>', UserViewSet.as_view( {
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',

    } ) )


]
