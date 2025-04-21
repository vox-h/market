from django.urls import path

import goods.views as views

app_name = 'goods'
urlpatterns = [
    path('search/', views.catalog, name='search'),
    path('<slug:category_slug>/', views.catalog, name='index'),
    path('product/<slug:product_slug>/', views.product, name='product'),
]
