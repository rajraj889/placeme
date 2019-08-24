from django.contrib import admin
from .models import Post,company,study


class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['name', 'content']
    prepopulated_fields = {'slug': ('name',)}
    

class studyAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['name', 'content']
    prepopulated_fields = {'slug': ('name',)}
    

admin.site.register(company)
admin.site.register(Post, PostAdmin)
admin.site.register(study, studyAdmin)
# Register your models here.
