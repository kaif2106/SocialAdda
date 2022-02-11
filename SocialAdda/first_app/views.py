from django.shortcuts import render
from first_app.forms import formName
from first_app.models import Conf

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

def confList(request):
    conf_lis = Conf.objects.all()
    return render(request, 'first_app/confList.html', {'conf_lis':conf_lis})