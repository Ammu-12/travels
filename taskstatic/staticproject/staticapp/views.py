from django.shortcuts import render
from .models import place
from .models import team

# Create your views here.
def ran(request):
    obj = place.objects.all()
    var= team.objects.all()
    return render(request, "index.html",{'result':obj,'res':var})

