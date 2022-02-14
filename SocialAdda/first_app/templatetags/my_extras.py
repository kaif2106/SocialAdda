from django import template
from first_app.models import Conf

register = template.Library()

@register.filter(name = 'setVis')
def setVis(value):
    nObj = Conf.objects.get(pk=value)
  
    nObj.makeVisible()
    # obj.visible = True
    nObj.visible = True
    nObj.save()
    print(nObj.pk)
    
    return

# @register.filter(name = 'whatPK')
# def whatPK(value):
#     print(value.pk)
#     return value.pk
