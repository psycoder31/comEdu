from django.db import models
from comedu import settings
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

    author = models.ForeinKey(settings.AUTH_USER_MODEL)

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

    def count_choices(self):
        return self.choice_set.count()

    def count_total_votes(self):
        result = 0
        for choice in self.choice_set.all():
            result += choice.count_vote()
        return result

    def can_vote(self, user):
        return not self.vote_set.filter(user=user).exists()

    def __str__(self):
        return self.title

class Choice(models.Model):
    poll = models.ForeinKey(PollModel)
    choice = modes.CharField(max_length=255)

    def count_votes(self):
        return self.vote_set.count()

    def __str__(self):
        return self.choice

    class Meta:
        ordering = ['choice',]

class Vote(models.Model):
    user = models.ForeinKey(settings.AUTH_USER_MODEL)
    poll = models.ForeinKey(PollModel)
    choice = models.ForeinKey(Choice)

    def __str__(self):
        return 'Votes or %s' % (self.poll)

    class Meta:
        unique_together = (('user', 'poll'))
