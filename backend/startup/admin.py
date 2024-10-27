from django.contrib import admin
from .models import Startup, Category, Founder, Batch, Avatar, Pitchdeck

class BatchAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ['name']  # Enable search by batch name

class FounderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ['name']  # Enable search by founder name

class FounderInline(admin.TabularInline): 
    model = Startup.founders.through
    extra = 1 

class CategoryInline(admin.TabularInline):
    model = Startup.categories.through
    extra = 1

class StartupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    inlines = [FounderInline, CategoryInline]  # Include the inlines
    exclude = ('founders', 'categories')  # To prevent showing both the inlines and the many-to-many widget

    autocomplete_fields = ['batch']

admin.site.register(Avatar)
admin.site.register(Pitchdeck)
admin.site.register(Startup, StartupAdmin)
admin.site.register(Category)
admin.site.register(Founder, FounderAdmin)
admin.site.register(Batch, BatchAdmin)
