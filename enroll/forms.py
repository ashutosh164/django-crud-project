from django import forms
from .models import Student


class StudentRegister(forms.ModelForm):
    class Meta:
        model = Student
        # fields = ['name','email','phone','address','password']
        fields = ['name','email','phone','address','image']

