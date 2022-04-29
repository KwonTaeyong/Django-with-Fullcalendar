import json

from django.shortcuts import render, HttpResponse
from ..models import Category, Packing, Factory, Product, Calendar
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm
from ..serializers.B2C_serializer import CalendarSerializer

def etclist(request):
    calendar_list = Calendar.objects.all()
    x = Calendar.objects.all()

    req = request.POST
    if req.get('alldata'):
        print(req.get('alldata'))
        testdata = json.loads(req.get('alldata'))
        for i in testdata:

            try:
                test_set = Calendar()
                test_set.title = i['title']
                test_set.start_data = i['start']
                test_set.end_data = i['end']
                test_set.allday = i['allday']
                test_set.save()
            except:
                pass




    result = []
    for iloc in Calendar.objects.all():
        tgdict = dict()
        tgdict['title'] = iloc.title
        tgdict['start'] = iloc.start_data.date().strftime("%Y-%m-%d")
        tgdict['end'] = iloc.end_data.date().strftime("%Y-%m-%d")
        result.append(tgdict)



    context = {
        'calendar': x,
        'calendar_list': calendar_list,
        'test': result
    }

    return render(request, 'B2C/etclist.html', context)
