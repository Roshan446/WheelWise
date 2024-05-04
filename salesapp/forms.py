from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import Form, ModelForm
from django import forms

from salesapp import models


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","email", "password1", "password2"]


class SigninForm(Form):
    username = forms.CharField()
    password = forms.CharField()

class BikeSellForm(ModelForm):
    class Meta:
        model = models.Bike
        exclude = [
            "user_object", 
            "is_active", 
            "updated_date", 
            "created_date", 
            "state_object", 
            "tag_object"]
        
class FeedbackForm(ModelForm):
    class Meta:
        model = models.Feedback
        fields = "__all__"
        