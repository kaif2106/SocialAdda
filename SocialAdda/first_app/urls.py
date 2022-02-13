from django.conf.urls import url
from . import views
#from first_app.views import confList

#Template tagging
app_name = 'first_app'

urlpatterns = [
    url(r'^$', views.confFill, name = 'confFill'),
    url(r'^confList/$', views.confList.as_view(), name = 'confList'),
]
