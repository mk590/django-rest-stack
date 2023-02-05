from django.forms import ModelForm
from .models import ques

class ques_add_form(ModelForm):
    class Meta:
        model=ques
        fields='__all__'