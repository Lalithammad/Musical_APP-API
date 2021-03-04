from django.shortcuts import render
# Create your views here.
import requests
import json
def index(request):
    li=[]
    li1=[]
    response = requests.get('http://localhost:8000/showdata/')
    # for i in response:
    #     id=i['show']['ID']
    #     title=i['show']['Title']
    #     contri=i['show']['Contributors']
    #     iswc=i['show']['ISWC']
    #     source=i['show']['Source']
    #     song=i['show']['Song']
    #     # li1.append(id)
    #     # li1.append(title)
    #     # li1.append(contri)
    #     # li1.append(iswc)
    #     # li1.append(source)
    #     li.append(song)
    #     type(i)
    #     type(response)
    # return render(request,"index.html",{'response':li1})
    return render(request,"index.html",{'response':response})
    
