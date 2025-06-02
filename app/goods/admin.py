from django.contrib import admin

from goods.models import Categories, Products


@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name',)


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'price', 'quantity', 'discount')
    list_editable = ('discount',)
    search_fields = ('name', 'description')
    list_filter = ('category', 'quantity', 'discount')
    fields = (
        'name',
        'category',
        'slug',
        'description',
        'image',
        ('price', 'discount'),
        'quantity'
    )
