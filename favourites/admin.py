from django.contrib import admin
from .models import Favourite


class FavouriteAdmin(admin.ModelAdmin):
    list_display = ['product', 'user']
    list_filter = ('product', 'user')
    ordering = ('product', )


admin.site.register(Favourite, FavouriteAdmin)
