from django.shortcuts import render

# Create your views here.

def home(request):

    sexos = [
        ('F' 'femenino'),
        ('M' 'masculino')
    ]

    return render(request, './Universidad/templates/index1.html', sexos)
