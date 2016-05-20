from django.shortcuts import render

def show(request):
    context = {}
    return render(request, 'profiles/show.html', context)
