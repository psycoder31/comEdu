from django.shortcuts import render, get_object_or_404,render_to_response, redirect, reverse
from django.views.generic import ListView
from .models import CalendarEvent
from .forms import CalendarForm
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib import messages


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
            form = CalendarForm(request.POST)##if method = POST save all content in site which sended request in form
            if form.is_valid():
                calendar = form.save(commit=False)##don't save directly, because should save after saving author info
                calendar.save()
                return redirect('/calendar/')
        else:
            form = CalendarForm()##????

        return render(request, 'comedu_calendar/calendar_new.html', {'form': form})##why give 'form':form???



def calendar_edit(request, pk=None, template_name='comedu_calendar/calendar_edit.html'):##pk값이 없으면 None
    if pk:
        calendar = get_object_or_404(CalendarEvent,id=pk)#저 모델에서 받은 pk값을 가지고 있는 모델 가져오기
    else:
        return HttpResponseForbidden()

    form = CalendarForm(request.POST or None, instance = calendar)##CalendarForm 쓰는데 calendar에 저장되어 있는 값을 디폴트로 설정
    if request.POST and form.is_valid():##제출 받으면
        form.save()
        return redirect('/calendar/%s' %(pk))

    return render(request, template_name, {
        'form': form
    })##실행 순서 : 버튼 누르면 url로 이동함과 동시에 pk값 전달 -> edit 뷰 실행 -> pk값을 가진 오브젝트를 CalendarEvent모델에서 찾아서 calendar에 저장 ->form에
      ##원래 글 저장 -> post안 눌렀으니까 맨 마지막 줄 실행 -> form이 보임 -> 사용자가 입력 -> 제출 -> POST->if POST 밑에 실행



def calendar_search(request):
    if request.GET['category'] == 'ti':
        if 'q' in request.GET and request.GET['q']:
            q = request.GET['q']
            calendars = CalendarEvent.objects.filter(title__icontains = q)
            return render_to_response('comedu_calendar/calendar_search.html', {'calendars':calendars,
                'query':q,} )
        else:
            return render_to_response('calendar_search.html',{'error':True,  })

    if request.GET['category'] == 'co':
        if 'q' in request.GET and request.GET['q']:
           q = request.GET['q']
           calendars = CalendarEvent.objects.filter(context__icontains = q)
           return render_to_response('comedu_calendar/calendar_search.html', {'calendars':calendars,
                'query':q,})
        else:
           return render_to_response('calendar_search.html',{'error':True,  })



def calendar_delete(request, pk):
    CalendarEvent(pk=pk).delete()
    return redirect('/calendar/')




# def calendar_success_popup(request,pk):
#     if 'y' in request.GET:
#         ##form.save()
#         return redirect('/calendar/')
#     else:
#         CalendarEvent.delete(pk=pk)
#         return redirect('/calendar/')
#
