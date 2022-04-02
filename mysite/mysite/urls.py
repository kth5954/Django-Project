from django.contrib import admin
from django.urls import path, include
from bookmark.views import BookmarkLV, BookmarkDV
from blog.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('bookmark/', include('bookmark.urls')),
    path('blog/', include('blog.urls')),
]
