from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.conf import settings


class Category(models.Model):
    name = models.CharField(unique=True, max_length = 100)
    slug = models.SlugField(unique=True, allow_unicode = True)
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField('TITLE', max_length=50)
    content = models.TextField('CONTENT')
    create_date = models.DateTimeField(
        'CREATE DATE',
        auto_now_add = True
        )
    modify_date = models.DateTimeField(
        'MODIFY DATE', auto_now = True
        )
    category = models.ForeignKey(Category, default = '')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default='')

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'my_post'
        ordering = ('-modify_date',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.id,))

    def get_previous_post(self):
        return self.get_previous_post_by_modify_date()

    def get_next_post(self):
        return self.get_next_post_by_modify_date()


class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default = '')
    message = models.TextField()
    create_date = models.DateTimeField(auto_now_add = True)
    modify_date = models.DateTimeField(auto_now = True)

####slug=공백의 - 채워줌, url은 공백 인식 x, allow_unicode는 한글 입력 가능
