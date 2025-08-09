from django.shortcuts import render
from django.views.generic import ListView


# Create your views here.
def about(request):
    return render(request, 'common/about.html')


# class HomePageView(ListView):
#