from aiogram.types import contact
from django.contrib import admin

# Register your models here.

from .models import News, Category, Contact


class NewsAdmin(admin.ModelAdmin):
    serarch_fields = ['title','body']
    list_display = ['title','body','status','published_time']
    list_filter = ['category','status']
    prepopulated_fields = {'slug':('title', )}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','nomi']





class ContactAdmin(admin.ModelAdmin):
    serarch_fields = ['user']
    list_display = ['user', 'email', 'msg']
    prepopulated_fields = {'email': ('user',)}


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.register(Contact, ContactAdmin)




