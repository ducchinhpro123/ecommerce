from django import forms
from .models import *


class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = '__all__'
        exclude = ['created_at', 'updated_at', 'user', 'products']
        labels = {
            'phone': 'Phone',
            'address': 'Address',
            'banner': 'Banner',
            'store_name': 'Store Name',
            'store_description': 'Store Description',

        }
        help_texts = {
            'phone': 'Enter your phone number',
            'address': 'Enter your address',
            'banner': 'Upload your store banner',
            'store_name': 'Enter your store name',
            'store_description': 'Enter your store description',
        }
        error_messages = {
            'phone': {
                'required': "Phone is required",
                'max_length': "Phone is too long",
            },
            'address': {
                'required': "Address is required",
                'max_length': "Address is too long",
            },
            'banner': {
                'required': "Banner is required",
            },
            'store_name': {
                'required': "Store name is required",
                'max_length': "Store name is too long",
            },
            'store_description': {
                'required': "Store description is required",
                'max_length': "Store description is too long",
            },
        }
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            'banner': forms.FileInput(attrs={'class': 'form-control'}),
            'store_name': forms.TextInput(attrs={'class': 'form-control'}),
            'store_description': forms.Textarea(attrs={'class': 'form-control'}),
        }

    #     save

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True):
        seller = Seller.objects.create(
            user=self.user,
            phone=self.cleaned_data['phone'],
            address=self.cleaned_data['address'],
            banner=self.cleaned_data['banner'],
            store_name=self.cleaned_data['store_name'],
            store_description=self.cleaned_data['store_description'],
        )
        return seller
