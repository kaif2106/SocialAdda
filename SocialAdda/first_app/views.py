from unicodedata import name
from urllib import request
from django.shortcuts import render
from first_app.forms import formName
from django import forms
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

def okok(request, cpk):
    
    pls = Conf.objects.get(pk=cpk)
    pls.visible = True
    pls.makeVisible()
    pls.save()
    return start(request)



class confList(generic.ListView):
    model = Conf
    template_name = 'first_app/confList.html'


# class adminList(generic.ListView):
#     model = Conf
#     template_name = 'first_app/adminList.html'
    

def adminList(request):
    lis = Conf.objects.all()
    # pls = Conf.objects.get(pk=34)
    # print("cla")
    # print(pls.pk)
    # pls.visibile = True
    # pls.makeVisible()
    # print(pls.visible)
    # pls.save()
    #a = Conf.objects.get()
    #form = forms.Form()

    if request.method == 'POST':   
        #print("yeah") 
        #print(request.POST.get('id'))
        pls = Conf.objects.get(pk=request.POST.get('id'))
        pls.visible = True
        pls.makeVisible()
        pls.save()
        return start(request)
    return render(request, 'first_app/adminList.html', {'object_list':lis})

# def adminList(request):
#     lis = Conf.objects.all()
#     return render(request, 'first_app/adminList.html', {'lis':lis})

