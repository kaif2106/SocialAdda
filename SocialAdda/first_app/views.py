import re
from django.shortcuts import redirect, render
from first_app.forms import formName, AddComment
from django import forms
from first_app.models import Conf, Comment
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
    pls.save()
    return redirect('/first_app/adminList/')



def adminList(request):
    lis = Conf.objects.all()
    if request.method == 'POST':   
        pls = Conf.objects.get(pk=request.POST.get('id'))
        pls.visible = True
        pls.save()
        
    return render(request, 'first_app/adminList.html', {'object_list':lis})


def deleteView(request, cpk):
    target = Conf.objects.get(pk = cpk)
    target.delete()
    return redirect('/first_app/adminList/')

class confList(generic.ListView):
    model = Conf
    template_name = 'first_app/confList.html'

def postDetail(request, cpk):
    all_comments = Comment.objects.all()
    print(all_comments)
    target = Conf.objects.get(pk = cpk)
    
    commentForm = AddComment()
    commentForm.id_conf = cpk
    if request.method == 'POST':
        print('g')
        if commentForm.is_valid():   
        #print(request.POST['text'])
        # commentForm = AddComment(request.POST)
        
            commentForm.text = request.POST['text']
            print('n')
            print(commentForm)
    
            commentForm.save(commit=True)
        
        
    return render(request, 'first_app/postPage.html', {'conf':target, 'commentForm':commentForm, 'all_comments':all_comments})
