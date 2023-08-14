from django.shortcuts import render

#Baby step - Usually a Model is used 
cats = [
  {'name': 'Lolo', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
  {'name': 'Carlita', 'breed': 'tortie', 'description': 'gentle and loving', 'age': 2},
]

# Create your views here.
#Always use request in your views functions
def home(request):
    #Return an HTTP response
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cats_index(request):
    return render(request, 'cats/index.html', {
        'cats' : cats
    })
