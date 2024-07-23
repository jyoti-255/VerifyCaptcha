from django import forms
from .models import NecModel
from captcha.fields import CaptchaField  
class NecForm(forms.ModelForm):
    captcha =CaptchaField()  

    class Meta:
        model = NecModel
        fields = ["name", "email", "captcha"]
