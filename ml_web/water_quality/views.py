from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Water
from .forms import WaterForm

import joblib

# Create your views here.



def getDataAndPredict(request):
    if request.method=='POST':
        form=WaterForm(request.POST)
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

        water=joblib.load("water_quality/static/WATER.pkl")
        prediction=water[6].predict(test_data)
        del dict['csrfmiddlewaretoken']
        prediction=water[6].predict(test_data)
        return render(request,'water_quality/water_form.html',{'form':form ,'ans':prediction[0]})

        print(dict)
    else:
        form=WaterForm()
         
    context={'form':form }
    
        
    return render(request,'water_quality/water_form.html',context)



