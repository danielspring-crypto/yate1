from django.contrib import admin

# Register your models here.
from .models import Category, Product 

admin.site.site_header = "Yate (ရိပ်)"
admin.site.site_title = "Admin Dashboard"
admin.site.index_title = "Admin Account ဖြင့်၀င်ရောက်နေပါသည်။"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug':('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
	list_filter = ['available', 'created', 'updated']
	list_editable = ['price', 'available']
	prepopulated_fields = {'slug':('name',)}
