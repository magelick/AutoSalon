from django.contrib import admin

from .models import BrandCar, ModelCar, BodyCar, Description


@admin.register(BrandCar)
class BrandAdmin(admin.ModelAdmin):
    search_fields = ('brand',)
    prepopulated_fields = {
        'slug': ('brand',)
    }
    ordering = ('brand',)


@admin.register(ModelCar)
class ModelAdmin(admin.ModelAdmin):
    search_fields = ('model',)
    list_display = ('model',)
    list_filter = ('model',)
    prepopulated_fields = {
        'slug': ('model',)
    }
    ordering = ('model',)


@admin.register(BodyCar)
class BodyAdmin(admin.ModelAdmin):
    search_fields = ('body',)
    list_display = ('body',)
    list_filter = ('body',)
    prepopulated_fields = {
        'slug': ('body',)
    }
    ordering = ('body',)


@admin.register(Description)
class DescriptionAdmin(admin.ModelAdmin):
    search_fields = ('price',)
    list_display = ('price', 'year_of_issue', 'mileage')
    ordering = ('year_of_issue', )
