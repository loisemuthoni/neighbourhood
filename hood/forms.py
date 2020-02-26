from .models import Business,NeighborHood,Userprofile,Post,Comment
from django import forms


class NewProfileForm(forms.ModelForm):
    class Meta:
        model=Userprofile
        exclude=['user_name']

class NewBusinessForm(forms.ModelForm):
    class Meta:
        model=Business
        exclude=['user']

class UpdateForm(forms.ModelForm):
    class Meta:
        model=Userprofile
        exclude=["profile_image","user_name","email"]