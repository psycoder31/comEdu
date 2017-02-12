from django.db import models
from django.core.urlresolvers import reverse

class Post(models.Model):
    title = models.CharField('TITLE',unique=True, max_length=50)
    description = models.CharField(
    "DESCRIPTION",
    max_length = 100,
    blank = True
    )
    content = models.TextField('CONTENT')
    create_date = models.DateTimeField(
        'CREATE DATE',
        auto_now_add = True
    )

    slug = models.SlugField('SLUG',
    # unique = True,
    allow_unicode = True,
    help_text = 'one word for title alias',
    default = '')

    modify_date = models.DateTimeField(
        'MODIFY DATE',
        auto_now = True
    )
### Pillow 다운받기 해결하고 이미지업로드기능넣기
    # photo = models.ImageField(blank = True, null = True)

###필드 타입 외 변수들 저장
    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'my_post'
        ordering = ('-modify_date',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.slug,))

    def get_previous_post(self):
        return self.get_previous_post_by_modify_date()

    def get_next_post(self):
        return self.get_next_post_by_modify_date()

class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.CharField(max_length = 10)
    message = models.TextField()
    create_date = models.DateTimeField(auto_now_add = True)
    modify_date = models.DateTimeField(auto_now = True)

####slug=공백의 - 채워줌, url은 공백 인식 x, allow_unicode는 한글 입력 가능
