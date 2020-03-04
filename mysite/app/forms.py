# users/forms.py

from django import forms
from .models import School

class SchoolForm(forms.ModelForm):
    """ 学校 """
    class Meta:
        model = School
        fields = ['name','address','date','num','per']

