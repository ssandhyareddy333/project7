from django.shortcuts import render

# Create your views here.
def biryani(request):
    return render(request,'biryani.html')
def dhosa(request):
    return render(request,'dhosa.html')