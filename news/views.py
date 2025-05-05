from django.shortcuts import render,get_object_or_404
from .models import News
# Create your views here.



def homepage(request):
    news = News.objects.all()
    return render(request,'home.html',{'news':news})


def detail(request,id):
    news = get_object_or_404(News,id=id)
    return render(request,'detail.html',{'abc':news})
