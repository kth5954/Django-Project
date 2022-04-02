from django.contrib import admin
from bookmark.models import Bookmark


@admin.register(Bookmark)  # decorator(어드민 사이트에 등록)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')
