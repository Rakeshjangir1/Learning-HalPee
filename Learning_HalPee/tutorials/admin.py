from django.contrib import admin
from .models.chapters import chapter, html_post, css_post

class Name_of_Chapter(admin.ModelAdmin):
    list_display = ['chapter_name']
admin.site.register(chapter,Name_of_Chapter)

class HTML_Post(admin.ModelAdmin):
    list_display = ['title','slug','updated_on','content','created_on','status']
    list_filter = ['status']
    search_fields = ['title', 'content']
admin.site.register(html_post, HTML_Post)

class CSS_Post(admin.ModelAdmin):
    list_display = ['title','slug','updated_on','content','created_on','status']
    list_filter = ['status']
    search_fields = ['title', 'content']
admin.site.register(css_post, CSS_Post)
