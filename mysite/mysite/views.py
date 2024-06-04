from django.shortcuts import render


def index(request):
    context = {
        'title':'Portofolio',
        'developer':'Arief Tri A',
    }
    return render(request, 'index.html', context)
