# -*- coding: utf-8 -*- 
from django.template import RequestContext
from django.template import Context, loader
from django.views.generic import simple
from django.shortcuts import render_to_response
import urllib
from skul.models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
import datetime
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
import django.core.files

def root_view(request):
    return render_to_response('home.html')

def student_register(request):
    if request.method=="GET":
        return render_to_response('studentregister.html')
    else:
        name=request.POST['name']
        code = request.POST['code']
        fname = request.POST['fname']
        uovog = request.POST['uovog']
        password = request.POST['password']
        regNumber = request.POST['regnumber']
        ynemNumber = request.POST['ynumber']
        address = request.POST['address']
        phone = request.POST['phone']
        email = request.POST['email']
        if request.POST['password'] == request.POST['password1']:
            Student.objects.create(
                username=convert_utf8(code),
                password = convert_utf8(password), 
                first_name=convert_utf8(name),
                last_name = convert_utf8(fname), 
                uovog=convert_utf8(uovog), 
                regNumber = convert_utf8(regNumber), 
                ynemNumber = convert_utf8(ynemNumber), 
                address = convert_utf8(address), 
                phone =convert_utf8(phone), 
                email = convert_utf8(email))
            content = '%s codetoi oyutan ta byrtgegdlee' %code               
            sendsms(phone, content)   
    return HttpResponseRedirect(reverse('home-student'))    

@permission_required('skul.add_sedev_lavlah')
def teacher_addtopic(request):
    if request.method=="GET":
        return render_to_response('TeacherSedevAdd.html')
    else:
        name=request.POST['name']
        ename = request.POST['ename']
        environment = request.POST['environment']
        sedev_filters = sedev_lavlah.objects.filter(name=name,english_name=ename)
        if not sedev_filters:
            sedev_lavlah.objects.create(name=convert_utf8(name), english_name=convert_utf8(ename),shaardlaga = convert_utf8(environment))
        else:
            return render_to_response('TeacherSedevAdd.html', {'error':1})
        return render_to_response('TeacherSedevAdd.html',{'success':1})


def student_home(request):
    return render_to_response('studentHome.html')

def teacher_home(request):
    return render_to_response('TeacherHome.html')

@login_required()
def FAQ_home(request):
    if request.method == "GET":
        aq = ansQue.objects.all()[:10]
        t = loader.get_template('FAQ.html')
        c = Context({
        'aq':aq,
        })
        return HttpResponse(t.render(c))
    else:
        question = request.POST['question']
        user = request.user
        ansQue.objects.create(
            question = question,
            answer = '',
            date = datetime.datetime.now(),
            user = user)
    return HttpResponseRedirect(reverse('home-FAQ'))

def contact(request):
    return render_to_response('contact.html')

def stuSedev(request):
    return render_to_response('studentSedev.html')

def convert_utf8(value):
    if isinstance(value, unicode):
        return value.encode('utf8')
    else:
        return value

def student_login(request):
    username = request.POST['name']
    password = request.POST['code']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return render_to_response('studentHome.html')
        else:
            return render_to_response('studentHome.html')
    else:
        return render_to_response('home.html')

@login_required()
def student_sedev(request):
    if request.method == "GET":
        sedevs = sedev_lavlah.objects.all()
        t = loader.get_template('studentSedev.html')
        teachers = teacher.objects.all()
        c = Context({
        'sedev': sedevs,
        'teacher': teachers
        })
        return HttpResponse(t.render(c))
    else:     
        sedev_id = request.POST['sedevs']
        teacher_id = request.POST['teachers']
        now = datetime.datetime.now()
        stuyear = ''
        t = 1
        if now.month>=6:
            stuyear = '%s-%s'%(now.year,now.year+1)
        else:
            stuyear = '%s-%s'%(now.year-1,now.year)
        sSedev = songoson_sedev.objects.filter(teacher_code=teacher_id, sedev_code=sedev_id)
        if not sSedev:
            songoson_sedev.objects.create(
                sedev_code = sedev_id, 
                tugsult_code = 1,
                date = datetime.date.today(),
                stu_year =  stuyear,
                teacher_code = teacher_id,
                student_code = request.user.username)
            return render_to_response('studentSedev.html',{'success':1})
        else:
            return render_to_response('studentSedev.html',{'error':1})
    return HttpResponseRedirect(reverse('sedev-student'))
 


@login_required()
def student_yzhuv(request):
    if request.method == "GET":
        yzlegs = yzleg.objects.all()
        nowyz  = yzleg.objects.filter(date__gt = datetime.date.today())
        t = loader.get_template('studentYzleg.html')
        c = Context({
        'yzlegs': yzlegs,
        'nowyz': nowyz,
        })
        return HttpResponse(t.render(c))

def contact_message(request):
    if request.method == "GET":
        return render_to_response('studentregister.html')
    else:
        name=request.POST['name']
        message = request.POST['message']
        email = request.POST['email']
        garchig = 'Холбогдох хүсэлт'
        to = 'ochma_lucky@yahoo.com'
        send_mail(garchig, message, email, [to], fail_silently=False)
    return render_to_response('home.html')

def sendsms(phone,content):
    ip = IP.objects.all()[0]
    urllib.urlopen('http://%s:%s/send?to=%s&content=%s'%(ip.ip,ip.port,phone,content))    
