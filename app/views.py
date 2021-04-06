from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Count, Case, When, Sum, IntegerField

from .models import *
#from .forms import *
import json

def hello_world(request):
    return render(request, 'home.html')


def device(request):
    if request.method == 'POST':
        form = TBL_DEVICE_INFO_FORM(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('device')
            except:
                pass
    else:
        form = TBL_DEVICE_INFO_FORM()

    context = {
        'form': form
    }
    return render(request, 'device.html', context)


def device_show(request):
    devices = TBL_DEVICE_INFO.objects.all()
    context = {
        'devices': devices
    }
    return render(request, 'device_show.html', context)


def device_edit(request, tbl_device_info_id):
    device = TBL_DEVICE_INFO.objects.get(id=tbl_device_info_id)
    if request.method == 'POST':
        form = TBL_DEVICE_INFO_FORM(request.POST)
        if form.is_valid():
            device.status = form.cleaned_data['status'] 
            device.station = form.cleaned_data['station']
            device.region = form.cleaned_data['region']
            device.install_data = form.cleaned_data['install_date']
            device.save()
    else:
        form = TBL_DEVICE_INFO_FORM(instance=device)
        
    context = {
        'form': form
    }
    return render(request, 'device_edit.html', context)


def device_destroy(request, tbl_device_info_id):
    device = TBL_DEVICE_INFO.objects.get(id=tbl_device_info_id)
    device.delete()
    return redirect('device_show')


def person(request):
    if request.method == 'POST':
        form = TBL_PERSTON_INFO_FORM(request.POST)
        if form.is_valid():
            try: 
                form.save()
                return redirect('person')
            except:
                pass
    else:
        form = TBL_PERSON_INFO_FORM()

    context = {
        'form': form
    }
    return render(request, 'person.html', context)


def person_show(request):
    persons = TBL_PERSON_INFO.objects.all()
    context = {
        'persons': persons
    }
    return render(request, 'person_show.html', context)


def person_edit(request, tbl_person_info_id):
    person = TBL_PERSON_INFO.objects.get(id=tbl_person_info_id)
    if request.method == 'POST':
        form = TBL_PERSON_INFO_FORM(request.POST)
        if form.is_valid():
            person.degree = form.cleaned_data['degree'] 
            person.has_mask = form.cleaned_data['has_mask']
            person.device_id = form.cleaned_data['device_id']
            person.save()
            return redirect('person_show')
    else:
        form = TBL_PERSON_INFO_FORM(instance = person)
        context = {
            'form': form
        }
        return render(request, 'person_edit.html', context)

def person_destroy(request, tbl_person_info_id):
    person = TBL_PERSON_INFO.objects.get(id=tbl_person_info_id)
    person.delete()
    return redirect('person_show')


def total_table(request):
    num = TBL_PERSON_INFO.objects.values('device_id').annotate(count=Count('device_id'))
    if request.method == 'GET':
        for i in range(num.count()):
            total = TBL_PERSON_INFO.objects.filter(device_id=num[i]['device_id'])
            mask = TBL_PERSON_INFO.objects.filter(device_id=num[i]['device_id'], has_mask=True)
            degree = TBL_PERSON_INFO.objects.filter(device_id=num[i]['device_id'], degree__gte=37.5)
            device_id = total[0].device_id
            total_pop = total.count()
            mask_pop = mask.count()
            high_temp_pop = degree.count()
            region = total[0].device_id.region

            if TBL_TOTAL_INFO.objects.filter(device_id=num[i]['device_id']):
                TBL_TOTAL_INFO.objects.filter(device_id=num[i]['device_id']).update(total_pop=total_pop, mask_pop=mask_pop, high_temp_pop=high_temp_pop)
            else:
                TBL_TOTAL_INFO.objects.create(device_id=device_id, total_pop=total_pop, mask_pop=mask_pop, high_temp_pop=high_temp_pop, region=region)
    total_table = TBL_TOTAL_INFO.objects.all()

    context = {
        'total_table': total_table
    }
    return render(request, 'total.html', context)






#@csrf_wxempt
def showmap(request, tbl_person_info_id):
    person = TBL_PERSON_INOF.objects.get(id=tbl_person_info_id)
    person_dict = {
        'lat': person.device_id.latitude,
        'lon': person.device_id.longitude,
        'station': person.device_id.station,
    }

    person_json = json.dumps(person_dict)
    return render(request, 'map.html', {'person_json': person_json})


def show_tjs(request):
    import pandas as pd
    import requests
    import json

    url = 'https://m.land.naver.com/cluster/ajax/articleList?rletTpCd=TJ&tradTpCd=A1&z=14&lat=37.5171001&lon=127.3344533&btm=37.4868331&lft=127.2879331&top=37.5473548&rgt=127.3809735&showR0=&totCnt=116&cortarNo='

    body = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Whale/2.8.108.15 Safari/537.36',
    }
    r = requests.get(url, headers=body)
    data = json.loads(r.text)
    tj_df = pd.json_normalize(data['body'])

    dictionary = {str(i): data['body'][i] for i in range(len(data['body']))}
    print(dictionary)



    return render(request, 'marker.html', {'tj_json': json.dumps(dictionary)})
