from django.db import models
from django.urls import reverse  # url 패턴을 만들어주는 함수


class Post(models.Model):
    title = models.CharField(verbose_name='TITLE', max_length=50)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text.')
    content = models.TextField('CONTENT')
    create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)  # 생성 시간
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)  # 수정 시간

    class Meta:
        verbose_name = 'post'  # 단수별칭
        verbose_name_plural = 'posts'  # 복수별칭
        db_table = 'blog_posts'  # 테이블이름(Default='blog_post')
        ordering = ('-modify_dt',)  # 'modify_dt' 기준 내림차순 정렬

    def __str__(self):  # 객체를 문자열로 표현
        return self.title

    def get_absolute_url(self):  # 이 메소드가 정의된 객체를 지칭하는 url 반환
        return reverse('blog:post_detail', args=(self.slug,))

    def get_previous(self):  # 최신 포스트 반환
        return self.get_previous_by_modify_dt()

    def get_next(self):  # -modify_dt 기준 예전 포스트 반환
        return self.get_next_by_modify_dt()


