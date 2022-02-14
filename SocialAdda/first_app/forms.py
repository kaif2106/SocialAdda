
from django import forms
from first_app.models import Conf

class formName(forms.ModelForm):
    class Meta:
        model = Conf
        fields = ['text']
        text = forms.CharField(max_length=100)

class voteForm(forms.Form):
    upVote = forms.BooleanField()
    downVote = forms.BooleanField()



   

    
