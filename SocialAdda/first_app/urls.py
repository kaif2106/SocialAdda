from django.conf.urls import url
from . import views

#Template tagging
app_name = 'first_app'

urlpatterns = [
    url(r'^$', views.confFill, name = 'confFill'),
    url(r'^confList/$', views.confList, name = 'confList'),
]