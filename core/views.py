from django.shortcuts import render

# Create your views here.
'''
/home
/about/
services/
store/
contact/
blog/
sample/

'''


def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request,'core/about.html')

def contact(request):
    return render(request,'core/contact.html') 

def store(request):
    return render(request,'core/store.html')

