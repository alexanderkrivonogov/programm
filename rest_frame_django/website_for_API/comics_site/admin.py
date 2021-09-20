from django.contrib import admin
from .models import Category, Comics


class ComicsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'grade', 'comment', 'photo', 'slug')
    prepopulated_fields = {'slug': ('name',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Comics, ComicsAdmin)
admin.site.register(Category, CategoryAdmin)
