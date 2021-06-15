from django.contrib import admin

from news.models import NewsModel


@admin.register(NewsModel)
class NewsModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'created_at']
    list_filter = ['title', 'content', 'created_at']
    search_fields = ['title']
