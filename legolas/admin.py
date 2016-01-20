from django.contrib import admin
from .models import *

# Register your models here.

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'parent']
    list_display_links = ['parent']


admin.site.register(Area)
admin.site.register(SubArea)
admin.site.register(Category)
admin.site.register(SubCategory ,SubCategoryAdmin)
admin.site.register(Store)
admin.site.register(User)
admin.site.register(Review)
admin.site.register(Comment)

