from socket import fromshare
from django import forms

class StudentForm(forms.Form):
    rn=forms.IntegerField()
    name=forms.CharField(max_length=50)
    adr=forms.CharField(max_length=50)
    fees=forms.FloatField()
    city=forms.CharField(max_length=50)
    