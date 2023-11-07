from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Team

# Create your views here.
def demo(request):
    leaf=Place.objects.all()
    zoo = Team.objects.all()
    return  render(request,"index.html",{'tree':leaf,'animal':zoo})


#def about(request):
    #return render(request,"about.html")
#def contact(request):
    #return HttpResponse("hello am contact")
