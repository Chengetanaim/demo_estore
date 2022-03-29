from django.urls import path

from .views import SearchResultsView, StoreSearchResultsView, ProductStoreSearchResultsView, SearchMobileResultsView
from . import views


urlpatterns = [
    path('result/', SearchResultsView.as_view(), name='search_results'),
    path('store_result/', StoreSearchResultsView.as_view(), name='store_search_results'),
    path('product_store_result/', ProductStoreSearchResultsView.as_view(), name='product_store_search_results'),
    path('search_mobile/', SearchMobileResultsView.as_view(), name='search_mobile_results'),
    path('mobile/', views.mobile, name='mobile')
]