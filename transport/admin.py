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
    search_fields = ('brand', 'model')
    list_display = ('brand', 'model',)
    list_filter = ('brand', 'model')
    prepopulated_fields = {
        'slug': ('model',)
    }
    ordering = ('brand', 'model')


@admin.register(BodyCar)
class BodyAdmin(admin.ModelAdmin):
    search_fields = ('model', 'body')
    list_display = ('model', 'body')
    list_filter = ('model', 'body')
    prepopulated_fields = {
        'slug': ('body',)
    }
    ordering = ('model', 'body')


@admin.register(Description)
class DescriptionAdmin(admin.ModelAdmin):
    search_fields = ('price',)
    list_display = ('price', 'year_of_issue', 'mileage')
    ordering = ('year_of_issue', )
