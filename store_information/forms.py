from django import forms
from .models import Item, EStore, ItemEstore, HotDeals


class ItemForm(forms.ModelForm):

   class Meta:
       model = Item
       fields = ['product_name', 'price', 'location', 'description', 'category', 'image1', 'image2', 'image3', 'image4']
       labels = {'product_name': 'Name', 'price': 'Price', 'location': 'Location', 'description': 'Description', 'image1':
                 'Image', 'image2': 'Image', 'image3': 'Image', 'image4': 'Image'}


class Create_EStoreForm(forms.ModelForm):
    class Meta:
        model = EStore
        fields = ['store_name', 'category', 'location', 'profile_pic']
        labels = {'store_name': 'Store Name', 'category': 'Category', 'location': 'Location', 'profile_pic': 'Profile Picture'}


class ItemEstoreForm(forms.ModelForm):
    class Meta:
        model = ItemEstore
        fields = ['product_name', 'price', 'description', 'category', 'estore', 'image1', 'image2', 'image3', 'image4']
        labels = {'product_name': 'Product Name', 'price': 'Price', 'description': 'Description', 'category': 'Category'
            , 'estore': 'Estore', 'image1': 'Image', 'image2': 'Image', 'image3': 'Image', 'image4': 'Image'}


class HotDealsForm(forms.ModelForm):
    class Meta:
        model = HotDeals
        fields = ['image', 'description']
        labels = {'image': 'Image', 'description': 'Description'}

