from django.urls import path, re_path
from blog import views


app_name = 'blog'
urlpatterns = [
    # example: /blog/
    path('', views.PostLV.as_view(), name='index'),
    # example: /blog/post/ (same as /blog/)
    path('', views.PostLV.as_view(), name='post_list'),
    # example: /blog/post/django-example/
    re_path(r'^post/(?P<slug>[-\w]+)/$',views.PostDV.as_view(),name='post_detail'),
    # example: /blog/archive/
    path('archive/',  views.PostAV.as_view(), name='post_archive'),
    # example: /blog/archive/2019/
    path('archive/<int:year>/', views.PostYAV.as_view(), name='post_year_archive'),
    # example: /blog/archive/2019/nov/
    path('archive/<int:year>/<str:month>/', views.PostMAV.as_view(), name='post_month_archive'),
    # example: /blog/archive/2019/nov/10/
    path('archive/<int:year>/<str:month>/<int:day>/', views.PostDAV.as_view(), name='post_day_archive'),
    # example: /blog/archive/today/
    path('archive/today/', views.PostTAV.as_view(), name='post_today_archive'),
]
