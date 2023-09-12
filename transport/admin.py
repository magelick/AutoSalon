from django.contrib import admin

from .models import BrandCar, ModelCar


@admin.register(BrandCar)
class BrandAdmin(admin.ModelAdmin):
    search_fields = ('brand',)
    prepopulated_fields = {
        'slug': ('brand',)
    }
    ordering = ('brand',)


@admin.register(ModelCar)
class ModelAdmin(admin.ModelAdmin):
    search_fields = ('brand',)
    list_display = ('brand', 'model',)
    list_filter = ('brand',)
    prepopulated_fields = {
        'slug': ('model', 'body', 'mileage', 'year_of_issue', 'engine_type', 'transmission', 'color')
    }
    ordering = ('brand', 'model')
