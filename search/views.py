from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from store_information.models import Item, EStore, ItemEstore, HotDeals
from django.contrib.auth.decorators import login_required


class SearchResultsView(ListView):
    model = Item
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list =  Item.objects.filter(
        Q(product_name__icontains=query) | Q(location__icontains=query)
        )
        return object_list


class StoreSearchResultsView(ListView):
    model = EStore
    template_name = 'store_search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list =  EStore.objects.filter(
        Q(store_name__icontains=query) | Q(location__icontains=query) | Q(category__icontains=query)
        )
        return object_list


class ProductStoreSearchResultsView(ListView):
    model = ItemEstore
    template_name = 'product_store_search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list =  ItemEstore.objects.filter(
        Q(product_name__icontains=query) | Q(category__icontains=query)
        )
        return object_list


class SearchMobileResultsView(ListView):
    model = Item
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Item.objects.filter(
        Q(product_name__icontains=query) | Q(location__icontains=query)
        )
        return object_list


def mobile(request):
    return render(request, 'mobile.html')