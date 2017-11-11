from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Subscriber


class AddressMixin(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['address_one', 'address_two', 'city', 'province']
        widgets = {
            'address_one':forms.TextInput(attrs={'class':'form-control'}),
            'address_two':forms.TextInput(attrs={'class':'form-control'}),
            'city': forms.TextInput(attrs={'class':'form-control'}),
            'province': forms.TextInput(attrs={'class':'form-control'}),
        }

    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
    #     self.fields['address_one'].label = 'Address one'
    #     self.fields['address_two'].label = 'Address two'
    #     self.fields['city'].label = 'City'
    #     self.fields['province'].label = 'Province'


# class SubscriberForm(AddressMixin,UserCreationForm):
    
#     class Meta:
#         # model = get_user_model()
#         model = User
#         fields = ('first_name','last_name','email','username','password1','password2')
#         widgets = {
#             'first_name':forms.TextInput(attrs={'class':'form-control'}),
#             'last_name':forms.TextInput(attrs={'class':'form-control'}),
#             'email': forms.TextInput(attrs={'class':'form-control'}),
#             'username': forms.TextInput(attrs={'class':'form-control'}),
#             'password1': forms.TextInput(attrs={'class':'form-control'}),
#             'password2': forms.TextInput(attrs={'class':'form-control'}),
#         }

#     def __init__(self,*args,**kwargs):
#         super(SubscriberForm, self).__init__(*args,**kwargs)
#         self.fields['first_name'].label = 'First Name'
#         self.fields['last_name'].label = 'Last Name'
#         self.fields['username'].label = 'Display Name'
#         self.fields['email'].label = 'Email Address'
#         self.fields['password1'].label = 'password1'
#         self.fields['password2'].label = 'password2'
#         self.fields['address_one'] = 'Address one'
#         self.fields['address_two'] = 'Address two'
#         self.fields['city'] = 'City'
#         self.fields['province'] = 'Province'


class SubscriberForm(AddressMixin,UserCreationForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control', 'type':'password'}))
    password2 = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control', 'type':'password'}))

    # class Meta:
    #     model = User
    #     fields = ('first_name','last_name','email','username','password1','password2')

    
    # def __init__(self,*args,**kwargs):
    #     AddressMixin.__init__(self,*args,**kwargs)
    #     # super().__init__(*args,**kwargs)
    #     self.fields['address_one'].label = 'Address one'
    #     self.fields['address_two'].label = 'Address two'
    #     self.fields['city'].label = 'City'
    #     self.fields['province'].label = 'Province'

