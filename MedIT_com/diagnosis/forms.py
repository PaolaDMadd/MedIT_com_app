from django import forms
from .models import Symptoms, DataEntry

class UserSymptoms(forms.Form):
    newList = Symptoms()
    symptom1 = forms.ChoiceField(label='1st Symptom', choices=newList.symptomList)
    symptom2 = forms.ChoiceField(label='2nd Symptom', choices=newList.symptomList)
    symptom3 = forms.ChoiceField(label='3rd Symptom', choices=newList.symptomList)
    symptom4 = forms.ChoiceField(label='4th Symptom', choices=newList.symptomList)
    symptom5 = forms.ChoiceField(label='5th Symptom', choices=newList.symptomList)
