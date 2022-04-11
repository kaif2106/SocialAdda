

from django.conf.urls import url
from django.urls import path
from . import views
#from first_app.views import confList

#Template tagging
app_name = 'first_app'

urlpatterns = [
    url(r'^$', views.confFill, name = 'confFill'),
    url(r'^confList/$', views.confList.as_view(), name = 'confList'),
    path(r'start', views.start, name = 'start'),
    path(r'adminList/', views.adminList, name = 'adminList'),
    path(r'add/<int:cpk>/', views.okok, name = "okok"),
    path(r'post/<int:cpk>/', views.postDetail, name = "postDetail"),
    path(r'delete/<int:cpk>/', views.deleteView, name = "deleteView"),
    

]
