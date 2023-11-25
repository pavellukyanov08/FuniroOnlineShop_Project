from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

admin.site.register(Menu)
admin.site.register(Category)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    exclude = ('cart_prods',)
    list_display = ['category', 'name', 'description',
                    'show_image', 'price', 'discount_price',
                    'availability_status', 'vote_total', 'vote_ratio',
                    'created', 'updated'
                    ]

    list_filter = ['name', 'price', 'availability_status']
    ordering = ('name', )

    def show_image(self, obj):
        if obj.img:
            return mark_safe(f"<img src='{obj.img.url}' width='50' height='50' />")
        return 'None'

    show_image.__name__ = 'Картинка'


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['owner', 'product', 'body', 'value', 'created']
    list_filter = ('owner', 'product')
    ordering = ('product', )


admin.site.register(Review, ReviewAdmin)

admin.site.register(ProductAvailability)
