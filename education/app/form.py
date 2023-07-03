from django import forms
from app.models import student
from app.models import courseregistration

class studentForm(forms.ModelForm):
    class Meta:
        model=student
        fields='__all__'

class studentForm2(forms.ModelForm):
    class Meta:
        model=courseregistration
        fields=['phoneno']