from django.contrib import admin

from .models import PollModel, Choice, Vote

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class PollAdmin(admin.ModelAdmin):
    model = PollModel
    inlines = (ChoiceInline,)
    list_display = ('title', 'count_choices', 'count_total_votes')

class VoteAdmin(admin.ModelAdmin):
    model = Vote
    list_display=('choice', 'user', 'poll')

admin.site.register(PollModel, PollAdmin)
admin.site.register(Vote, VoteAdmin)
