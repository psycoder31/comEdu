from django.shortcuts import render, get_object_or_404,render_to_response
from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView
from .models import CalendarEvent
from django.shortcuts import redirect, render, reverse
from .forms import CalendarForm
from django.http import HttpResponse
from django.template import RequestContext


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


def calendar_edit(request, pk=None, template_name='comedu_calendar/calendar_edit.html'):##pk값이 없으면 None
    if pk:
        calendar = get_object_or_404(CalendarEvent,id=pk)#저 모델에서 받은 pk값을 가지고 있는 모델 가져오기
    else:
        return HttpResponseForbidden()

    form = CalendarForm(request.POST or None, instance=calendar)##CalendarForm 쓰는데 calendar에 저장되어 있는 값을 디폴트로 설정
    if request.POST and form.is_valid():
        form.save()

        # Save was successful, so redirect to another page
        return render_to_response('comedu_calendar/calendar_all.html', RequestContext={'Calendars':form})#이 부분 수정

    return render(request, template_name, {
        'form': form
    })


def calendar_search(request):

    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        calendars = CalendarEvent.objects.filter(title__icontains = q)
        return render_to_response('comedu_calendar/calendar_search.html', {'calendars':calendars, 'query':q})
    else:
        return render_to_response('calendar_search.html',{'error':True})
