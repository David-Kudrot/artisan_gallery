from django.contrib import admin
from artwork.models import Artwork, Category
# Register your models here.


class ArtworkAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']

admin.site.register(Artwork, ArtworkAdmin)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name', 'slug']
admin.site.register(Category, CategoryAdmin)