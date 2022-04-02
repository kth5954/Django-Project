
from re import template
from statistics import mode
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView
from blog.models import Post

class HomeView(TemplateView):
    template_name = 'home.html'

class PostLV(ListView): 
    model = Post 
    template_name = 'blog/post_all.html' 
    context_object_name = 'posts'  # 컨텍스트 변수명 = posts(디폴트: object_list)
    paginate_by = 2  # 한 페이지에 보여주는 객체 리스트 숫자 2

class PostDV(DetailView):  # DetailView: 테이블로부터 특정 객체를 가져와 상세정보 출력
    model = Post  

class PostAV(ArchiveIndexView):  # ArchiveIndexView: 테이블로부터 객체 리스트를 가져와 날짜 필드를 기준으로 최신 객체 출력
    model = Post  
    date_field = 'modify_dt'  

class PostYAV(YearArchiveView):  # YearArchiveView: 테이블로부터 날짜 필드 연도를 기준으로 객체리스트를 가져와 그 객체들이 속한 월을 출력
    model = Post  
    date_field = 'modify_dt'  
    make_object_list = True  # True 면 해당 연도에 해당하는 객체의 리스트를 만들어서 템플릿에 넘겨줌

class PostMAV(MonthArchiveView): # MonthArchiveView: 테이블로부터 날짜 필드 연월을 기준으로 객체리스트 출력
    model = Post  
    date_field = 'modify_dt'  

class PostDAV(DayArchiveView):  # DayArchiveView: 테이블로부터 날짜 필드 연월일을 기준으로 객체리스트 출력
    model = Post  
    date_field = 'modify_dt'  

class PostTAV(TodayArchiveView):  # TodayArchiveView: 테이블로부터 오늘을 기준으로 객체리스트 출력
    model = Post 
    date_field = 'modify_dt' 

