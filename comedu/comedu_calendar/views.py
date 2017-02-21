from django.shortcuts import render, get_object_or_404,render_to_response, redirect, reverse
from django.views.generic import ListView
from .models import CalendarEvent
from .forms import CalendarForm
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.conf import settings

# Create your views here.


class CalendarEventLV(ListView):
        model = CalendarEvent
        template_name = 'comedu_calendar/calendar_all.html'
        context_object_name = 'calendars'
        paginate_by = 10



def cal_detail(request, pk):
    if not request.user.is_authenticated:
        return redirect('/calendar/')
    else:
        queryset2 = get_object_or_404(CalendarEvent, pk=pk)
        return render(request, 'comedu_calendar/calendar_detail.html', {'calendar':queryset2})



def calendar_new(request):
    if not request.user.is_authenticated:
        return redirect('/calendar/')
    else:
        if request.method == "POST":
                form = CalendarForm(request.POST)##if method = POST save all content in site which sended request in form
                if form.is_valid():
                    calendar = form.save(commit=False)
                    calendar.save()
                    return redirect('/calendar/')
        else:
            form = CalendarForm()##????

        return render(request, 'comedu_calendar/calendar_new.html', {'form': form})##why give 'form':form???



def calendar_edit(request, pk=None, template_name='comedu_calendar/calendar_edit.html'):##pk값이 없으면 None
    if not request.user.is_authenticated:
        return redirect('/calendar/')
    else:
        if pk:
            calendar = get_object_or_404(CalendarEvent,id=pk)#저 모델에서 받은 pk값을 가지고 있는 모델 가져오기

        form = CalendarForm(request.POST or None, instance = calendar)##CalendarForm 쓰는데 calendar에 저장되어 있는 값을 디폴트로 설정

        if request.POST and form.is_valid():##제출 받으면
            form.save()
            return redirect('/calendar/%s' %(pk))
        if request.user == calendar.author:
            return render(request, template_name, {
                'form': form
            })



def calendar_search(request):
    if request.GET['category'] == 'ti':
        if request.GET['q']:
            q = request.GET['q']
            search_results = CalendarEvent.objects.filter(title__icontains = q)
            paginator = Paginator(search_results, 10)
            page = request.GET.get('page', '1')
            try:
                results = paginator.page(page)
            except PageNotAnInteger:
                results = paginator.page(1)
            except EmptyPage:
                results = paginator.page(paginator.num_pages)
            return render_to_response('comedu_calendar/calendar_search.html', {'calendars':results, 'query':q})
        else:
            return render_to_response('comedu_calendar/calendar_search.html')

    if request.GET['category'] == 'co':
        if request.GET['q']:
           q = request.GET['q']
           search_results = CalendarEvent.objects.filter(context__icontains = q)
           paginator = Paginator(search_results, 10)
           page = request.GET.get('page', '1')
           try:
               results = paginator.page(page)
           except PageNotAnInteger:
               results = paginator.page(1)
           except EmptyPage:
               results = paginator.page(paginator.num_pages)
           return render_to_response('comedu_calendar/calendar_search.html', {'calendars':results, 'query':q})
        else:
           return render_to_response('comedu_calendar/calendar_search.html')

    if request.GET['category'] == 'au':
        if request.GET['q']:
           q = request.GET['q']
           search_results = CalendarEvent.objects.filter(author__username__contains = q)
           paginator = Paginator(search_results, 10)
           page = request.GET.get('page', '1')
           try:
               results = paginator.page(page)
           except PageNotAnInteger:
               results = paginator.page(1)
           except EmptyPage:
               results = paginator.page(paginator.num_pages)
           return render_to_response('comedu_calendar/calendar_search.html', {'calendars':results, 'query':q})
        else:
           return render_to_response('comedu_calendar/calendar_search.html')


def calendar_delete_popup(request, pk):
    if not request.user.is_authenticated:
        return redirect('/calendar/')
    else:
        return render_to_response('comedu_calendar/calendar_delete.html',{'pk':pk})



def calendar_delete(request, pk):

    if request.GET['answer']=="YES":
        CalendarEvent(pk=pk).delete()
        return redirect('/calendar/')
    else:
        return redirect('/calendar/%s' %(pk))


def calendar_show(request):
    calendars = CalendarEvent.objects.all()
    return render(request, 'comedu_calendar/calendar.html', {'calendars':calendars})


def calendar_success_popup(request):
    return render(request,"comedu_calendar/calendar_register_popup.html")
