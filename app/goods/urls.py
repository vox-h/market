from django.urls import path

import goods.views as views

app_name = 'goods'

urlpatterns = [
    path('', views.catalog, name='index'),
    path('product/', views.product, name='product'),
]
