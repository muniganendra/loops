from django.shortcuts import render

# Create your views here.
def loops(request):
    d={'k':10,'b':'muniganendra','c':[12,34,24,234,2345],'d':(1,2,3,4,5),'e':{'p':1,'j':90}}
    return render(request,'loops.html',d)
