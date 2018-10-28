from django.contrib import admin
from .models import ProductRequest

# Register your models here.


@admin.register(ProductRequest)
class ProductRequestAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductRequest._meta.get_fields()]