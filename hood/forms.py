from .models import Business,NeighborHood,Userprofile,Post,Comment
from django import forms


class NewProfileForm(forms.ModelForm):
    class Meta:
        model=Userprofile
        exclude=['user_name']
