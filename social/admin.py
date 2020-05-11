from django.contrib import admin
from .models import Link
# Register your models here.

class LinkAdmin(admin.ModelAdmin):
    readonly_fields= ('created','updated')
    list_display = ('name',)

    def get_readonly_fields(self,request,obj=None):
        if request.user.groups.filter(name="Personal").exists():
            return ('created','updated','key','name')
        else:
            return ('created','updated')
admin.site.register(Link,LinkAdmin)










'''
aca vas a crear las configuraciones para el admin, que queres que se vea y toda esa gilada

'''