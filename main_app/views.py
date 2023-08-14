from django.shortcuts import render

# Create your views here.
#Always use request in your views functions
def home(request):
    #Return an HTTP response
    return render(request, 'home.html')

