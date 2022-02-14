from urllib import request
from django.shortcuts import render
from first_app.forms import formName

from first_app.models import Conf
from django.views import generic

# Create your views here.

def start(request):
    return render(request, 'first_app/start.html')

def confFill(request):
    form = formName()
    if request.method == 'POST':
        form = formName(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return start(request)
        else:
            print('ERROR IN FORM')
    cd = {'form':form}
    return render(request, 'first_app/confFill.html', cd)


class confList(generic.ListView):
    model = Conf
    template_name = 'first_app/confList.html'


# class adminList(generic.ListView):
#     model = Conf
#     template_name = 'first_app/adminList.html'

def adminList(request):
    lis = Conf.objects.all()
    pls = Conf.objects.get(pk=34)
    print("cla")
    print(pls.pk)
    pls.visibile = True
    pls.makeVisible()
    print(pls.visible)
    #a = Conf.objects.get()
    if request.method == 'POST':    
        print("aya")
        for obj in lis:
            if obj.pk in request.POST:
                print("gotcha "+obj.pk)
    return render(request, 'first_app/adminList.html', {'lis':lis})

# def adminList(request):
#     lis = Conf.objects.all()
#     return render(request, 'first_app/adminList.html', {'lis':lis})

