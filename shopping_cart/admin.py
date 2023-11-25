from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import ShoppingCart


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'show_image', 'quantity', 'user']
    list_filter = ['name', 'price', 'user']
    ordering = ('product',)

    def show_image(self, obj):
        if obj.img:
            return mark_safe(f"<img src='{obj.img.url}' width='50' height='50' />")
        return 'None'

    show_image.__name__ = 'Картинка'
