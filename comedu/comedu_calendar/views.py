from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView
from .models import CalendarEvent
from django.shortcuts import redirect
from .forms import CalendarForm



# Create your views here.


class CalendarEventLV(ListView):
        model = CalendarEvent
        template_name = 'comedu_calendar/calendar_all.html'
        context_object_name = 'calendars'
        paginate_by = 10


def cal_detail(request, pk):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        queryset2 = get_object_or_404(CalendarEvent, pk=pk)
        return render(request, 'comedu_calendar/calendar_detail.html', {'calendar':queryset2})


def calendar_new(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        if request.method == "POST":
            form = CalendarForm(request.POST)
            if form.is_valid():
                calendar = form.save(commit=False)
                calendar.save()
                return render(request, 'comedu_calendar/calendar_success.html')
        else:
            form = CalendarForm()
        return render(request, 'comedu_calendar/calendar_new.html', {'form': form})


def calendar_edit(request,pk):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        if request.method == "POST":
            form = CalendarForm(request.POST, pk=calendar.pk)
            if form.is_valid():
                calendar = form.save(commit=False)
                calendar = CalendarEvent.object.get(pk=calendar.pk)
                calendar.save()
                return redirect('calendar_edit', pk=calendar.pk)
        else:
            form = CalendarForm()
        return render(request, 'comedu_calendar/calendar_edit.html', {'form': form})
