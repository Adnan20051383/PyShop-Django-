from django.shortcuts import render


def show_index(request):
    return render(request, 'pp.html')

