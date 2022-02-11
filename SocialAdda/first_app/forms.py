from django import forms
from first_app.models import Conf

class formName(forms.ModelForm):
    class Meta:
        model = Conf
        fields = '__all__'