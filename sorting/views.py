from django.shortcuts import render
from store_information.models import ItemEstore, Item, EStore, HotDeals
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required()
def clothing(request):
    clothing = Item.objects.filter(category='Clothing')
    clothing_estore = EStore.objects.filter(category='Clothing')
    context = {'clothing': clothing, 'clothing_estore': clothing_estore}
    return render(request, 'sorting/clothing.html', context)


@login_required()
def electronics(request):
    electronics = Item.objects.filter(category='Electronics')
    electronics_estore = EStore.objects.filter(category='Electronics')
    context = {'electronics': electronics, 'electronics_estore': electronics_estore}
    return render(request, 'sorting/electronics.html', context)


@login_required()
def homeware(request):
    homeware = Item.objects.filter(category='Homeware')
    homeware_estore = EStore.objects.filter(category='Homeware')
    context = {'homeware': homeware, 'homeware_estore': homeware_estore}
    return render(request, 'sorting/homeware.html', context)


@login_required()
def other(request):
    other = Item.objects.filter(category='Other')
    other_estore = EStore.objects.filter(category='Other')
    context = {'other': other, 'other_estore': other_estore}
    return render(request, 'sorting/other.html', context)


@login_required()
def clothing_estore(request):
    clothing_estore = EStore.objects.filter(category='Clothing')
    context = {'clothing_estore': clothing_estore}
    return render(request, 'sorting/clothing_estore.html', context)


@login_required()
def electronics_estore(request):
    electronics_estore = EStore.objects.filter(category='Electronics')
    context = {'electronics_estore': electronics_estore}
    return render(request, 'sorting/electronics_estore.html', context)


@login_required()
def homeware_estore(request):
    homeware_estore = EStore.objects.filter(category='Homeware')
    context = {'homeware_estore': homeware_estore}
    return render(request, 'sorting/homeware_estore.html', context)


@login_required()
def other_estore(request):
    other_estore = EStore.objects.filter(category='Other')
    context = {'other_estore': other_estore}
    return render(request, 'sorting/other_estore.html', context)


@login_required()
def cosmetics_estore(request):
    cosmetics_estore = EStore.objects.filter(category='Cosmetics')
    context = {'cosmetics_estore': cosmetics_estore}
    return render(request, 'sorting/cosmetics_estore.html', context)


@login_required()
def vehicles_estore(request):
    vehicles_estore = EStore.objects.filter(category='Vehicles')
    context = {'vehicles_estore': vehicles_estore}
    return render(request, 'sorting/vehicles_estore.html', context)