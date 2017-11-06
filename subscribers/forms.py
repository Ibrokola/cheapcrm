from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Subscriber

class AddressMixin(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ('address_one', 'address_two', 'city', 'province')
        widgets = {
            'address_one':forms.TextInput(attrs={'class':'form-control'}),
            'address_two':forms.TextInput(attrs={'class':'form-control'}),
            'city': forms.TextInput(attrs={'class':'form-control'}),
            'province': forms.TextInput(attrs={'class':'form-control'}),
        }


class SubscriberForm(AddressMixin,UserCreationForm):
    
    class Meta:
        model = get_user_model()
        fields = ('first_name','last_name','email','username','password1','password2')
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'password1': forms.TextInput(attrs={'class':'form-control'}),
            'password2': forms.TextInput(attrs={'class':'form-control'}),
        }

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['first_name'] = 'First Name'
        self.fields['last_name'] = 'Last Name'
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Address'
