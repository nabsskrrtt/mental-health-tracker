from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'npm' : '2306275191',
        'name': 'Nabila Maharani Putri',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)