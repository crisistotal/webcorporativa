from django.contrib import admin
from .models import Category, Post
from django.contrib.auth.models import User


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields= ('created','updated')
    search_fields = ['name']

class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display = ('title','author','published','post_categories')
    ordering = ('author', 'published')
    search_fields = ('title','content','author__username','categories__name')
    date_hierarchy = 'published'
    list_filter = ('author__username','categories__name')


    def post_categories(self,obj):
        '''
            Este metodo de devuelve las categorias del post con en forma de tupla por eso
            arranca con la " ', ' " 
        '''
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])

    post_categories.short__description = 'Categorias'

admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)