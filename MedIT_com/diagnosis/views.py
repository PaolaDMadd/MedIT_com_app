from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserSymptoms
from .data.prediction_model import NaiveBayes
from .models import DataEntry
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = UserSymptoms(request.POST)
        if form.is_valid():
            s1 = form.cleaned_data['symptom1']
            s2 = form.cleaned_data['symptom2']
            s3 = form.cleaned_data['symptom3']
            s4 = form.cleaned_data['symptom4']
            s5 = form.cleaned_data['symptom5']
            result = NaiveBayes(s1,s2,s3,s4,s5)
            newEntry = DataEntry(symptom1=s1, symptom2=s2, symptom3=s3, symptom4=s4, symptom5=s5, diagnosis=result)
            newEntry.save()
            print('Entry was create !!!!!!!')
            return render(request, 'diagnosis/diagnosis.html', { 'form':form, 'result':result })
    else:
        form = UserSymptoms()
    return render(request, 'diagnosis/diagnosis.html', { 'form':form })


def history(request):
    # userHistory = get_user_history()
    # tomato = "tasty tomato"
    # displayHistory = {'potato': tomato}
    # for DataEntry in userHistory:
    #     displayHistory.append(f'<li> {DataEntry} <li>')
    return render(request, 'diagnosis/history.html')

@login_required
def profile(request):
    return render(request, 'diagnosis.profile.html' )