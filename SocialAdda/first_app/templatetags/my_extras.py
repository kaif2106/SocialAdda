from django import template
from first_app.models import Conf

register = template.Library()

# @register.filter(name = 'setVis')
# def setVis(obj):
#     nObj = Conf.objects.get(pk=obj.pk)
  
#     # obj.makeVisible()
#     # obj.visible = True
#     nObj.visible = True
#     print(nObj.pk)
    
#     return

# @register.filter(name = 'whatPK')
# def whatPK(value):
#     print(value.pk)
#     return value.pk
