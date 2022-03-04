from django.urls import path 
from . import views


urlpatterns = [
   
    path('', views.store, name='store'),
    path('brand/<brand_slug>/', views.store, name='products_by_brand'),

    path('category/<category_slug>/', views.store, name='products_by_category'),

    path('category/<category_slug>/<product_slug>/', views.product_detail, name='product_detail'),
    path('search/', views.search, name='search'),
    path('searchprice/', views.searchprice, name='searchprice'),

    path('submit_review/<int:product_id>/', views.submit_review, name='submit_review'),
]
   
