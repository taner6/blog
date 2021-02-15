from django.contrib import admin
from .models import Article,Comment

admin.site.register(Comment)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","author","created_date"]
    list_display_links = ["title","author","created_date"]
    search_fields = ["content"]
    list_filter = ["created_date"]
    actions = None
    class Meta:
        model = Article