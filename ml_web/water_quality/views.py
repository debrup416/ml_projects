from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Water
from .forms import WaterForm

import joblib

# Create your views here.


def result(request):
    if request.method=='POST':
        temp=[]
        dict={}
        for x in request.POST:
            print(request.POST[x])
            dict[x]=request.POST[x]
            temp.append(request.POST[x])

        temp.pop(0)
        test_data=[]
        test_data.append(temp)
        print(test_data)

        water=joblib.load("water_quality/WATER.pkl")
        prediction=water[6].predict(test_data)
        del dict['csrfmiddlewaretoken']

        print(dict)
         
        context={'feilds':dict.items() ,'ans':prediction[0]}


    return render(request,'water_quality/result.html',context)

     



def getData(request):
    form=WaterForm()
        

    context={'form':form}
    return render(request,'water_quality/water_form.html',context)

