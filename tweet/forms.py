from django import forms # type: ignore
from .models import Tweet
from .models import User
from django.contrib.auth.forms import UserCreationForm  # type: ignore
class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content', 'image']
        
class userRegisterationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
   