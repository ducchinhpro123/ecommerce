from django.contrib import admin

from product.models import Product
# Register your models here.

from .models import *


class ProductInline(admin.TabularInline):
    model = Product
    extra = 0


class SellerAdmin(admin.ModelAdmin):
    list_display = ['store_name', 'user', 'phone', 'address', 'created_at', 'updated_at', 'products']
    search_fields = ['store_name', 'user', 'phone', 'address']
    list_filter = ['created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']
    inlines = [ProductInline]

    # Display product that belongs to the seller
    def products(self, obj):
        return ", ".join([product.name for product in obj.product_set.all()])


admin.site.register(Seller, SellerAdmin)
