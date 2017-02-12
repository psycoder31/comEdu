from django.db import models

import datetime

# Create your models here.


class PollModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    start_date = models.DateTimeField(
        blank=False,
        default=datetime.datetime.now,
        )
    end_date = models.DateTimeField(
        blank=True,
        default=datetime.datetime.now,
        )
    agree = models.IntegerField(name='찬성', blank=True, null=True)

    disagree = models.IntegerField(name='반대',blank=True, null=True)

    abstention = models.IntegerField(name='기권',blank=True, null=True)

    author = models.CharField(name='작성자',blank=True, max_length=100)

    category = models.CharField(
        name='분류',
        choices=(
            ('ergent', '긴급'),
            ('events', '행사'),
            ('comedu', '과사'),
        ),
        default='ergent',
        blank=True,
        max_length=10,
    )
