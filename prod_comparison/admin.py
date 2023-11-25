from django.contrib import admin
from .models import Compare


class CompareAdmin(admin.ModelAdmin):
    list_display = ['product', 'user']
    list_filter = ['product', 'user']
    ordering = ('product',)


admin.site.register(Compare, CompareAdmin)
