from django.shortcuts import render
from  app.models import *
from django.db.models.functions import Length
from django.db.models import Q
# Create your views here.
def display_topic(request):
    QST=Topic.objects.all()
    QST=Topic.objects.filter(topic_name='sql')
    QST=Topic.objects.all()

    d={'topic':QST}
    return render(request,'display_topic.html',d)

def diplay_webpage(request):
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(name='siva sanju')
    QSW=Webpage.objects.exclude(name='siva sanju')
    QSW=Webpage.objects.all()[:4]
    QSW=Webpage.objects.all().order_by('topic_name')
    QSW=Webpage.objects.all().order_by('-topic_name')
    QSW=Webpage.objects.filter(topic_name='java').order_by('-name')
    QSW=Webpage.objects.order_by(Length('name'))
    QSW=Webpage.objects.order_by(Length('name').desc())
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(url__startswith='https')
    QSW=Webpage.objects.filter(url__endswith='com')
    QSW=Webpage.objects.filter(name__startswith='anil')
    QSW=Webpage.objects.filter(name__endswith='r')
    QSW=Webpage.objects.filter(name__contains='s')
    QSW=Webpage.objects.filter(name__regex='\w{5}')
    QSW=Webpage.objects.filter(name__in=['sanju','anil'])
    QSW=Webpage.objects.filter(Q(topic_name='java')|Q(name='anil'))
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(Q(topic_name='java') & Q(url__endswith='in'))
    d={'webpage':QSW}
    return render(request,'display_webpage.html',d)

def display_accesrecords(request):
    QSA=AccessRecords.objects.all()
    QSA=AccessRecords.objects.all().order_by('date')
    QSA=AccessRecords.objects.filter(date='2021-09-06')
    QSA=AccessRecords.objects.filter(date__gt='2021-09-06')
    QSA=AccessRecords.objects.filter(date__gte='2021-09-06')
    QSA=AccessRecords.objects.filter(date__lt='2021-09-06')
    QSA=AccessRecords.objects.filter(date__lte='2021-09-06')
    QSA=AccessRecords.objects.filter(date__year='2022')
    QSA=AccessRecords.objects.filter(date__month='09')
    QSA=AccessRecords.objects.filter(date__day='06')
    QSA=AccessRecords.objects.filter(date__year__gt='2021')
    d={'AccessRecords':QSA}
    return render(request,'display_accessrecords.html',d)

def update_webpage(request):
    QSW=Webpage.objects.all()
    d={'webpage':QSW}
    return render(request,'display_webpage.html',d)