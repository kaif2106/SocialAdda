from django import forms

from first_app.models import Conf

class formName(forms.ModelForm):
    class Meta:
        model = Conf
        fields = ['heading', 'text']
        
        widgets = {
            'heading': forms.Textarea(attrs={
                'class':'',
                'style':'max-width: 900px; color: white; background-color: #1a1a1b; resize: none;',
                'placeholder':'Heading',
                'rows':'1',
                'cols':'90'
            }),
            'text': forms.Textarea(attrs={
                'class':'',
                'style':'max-width: 900px; color: white; background-color: #1a1a1b;',
                'placeholder':'Text',
                'cols': '90'
            })
        }
        # heading = forms.CharField(max_length=200)
        # text = forms.CharField(max_length=100)

class AddComment(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={
        'style':'max-width: 900px; color: white; background-color: #1a1a1b;',
        'placeholder':'Comment',
        'rows':5,
        'cols':90
    }))

    # text = forms.CharField()
    # fields = ['text']
    # widgets = {
    #     'text': forms.Textarea(attrs={
    #         'class':'',
    #         'style':'max-width: 900px; color: white; background-color: #1a1a1b;',
    #         'placeholder':'Text',
    #         'cols': '90'
    #     })
    # }
    # class Meta:
    #     model = Comment
    #     fields = ['text']
    #     widgets = {
    #         'text': forms.Textarea(attrs={
    #             'class':'',
    #             'style':'max-width: 900px; color: white; background-color: #1a1a1b;',
    #             'placeholder':'Text',
    #             'cols': '90'
    #         })
    #     }

        

class voteForm(forms.Form):
    upVote = forms.BooleanField()
    downVote = forms.BooleanField()



   

    
