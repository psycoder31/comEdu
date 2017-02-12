from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class CalendarEvent(models.Model):

    title = models.CharField('Title',max_length=255)
    context = models.TextField("context")
    start = models.DateTimeField('Start Date')
    end = models.DateTimeField('End Date', null=True,
                               blank=True)
    department = '과행사'
    personal = '개인행사'
    anniversary = '연중행사'
    classify_choice = (
        (department,'과행사'),
        (personal, '개인행사'),
        (anniversary, '연중행사'),
    )
    classify = models.CharField(max_length = 20, choices = classify_choice, default = department)

    def __str__(self):
        return self.title

class search(models.Model):
    search = models.CharField('검색', max_length=50)
