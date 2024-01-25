from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class new_user_form(UserCreationForm):
    email=forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class":"focus:outline-none",
                "placeholder":"Enter email...",
            }
        ),
    )
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class":"focus:outline-none",
                "placeholder":"Enter username...",
            }
        ),
    )
    password1=forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class":"focus:outline-none",
                "placeholder":"Enter password...",
            }
        ),
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class":"focus:outline-none",
                "placeholder":"Re-enter password...",
            }
        ),
    )

    class Meta:
        model=User
        fields=("username","email","password1","password2")

#    def save(self,commit=True):
#        user = super(new_user_form,self).save(commit=False)
#       user.email=self.cleaned_data['email']
#       if commit:
#           user.save()
#      return user