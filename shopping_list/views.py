from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
def dispaly(request):
    
    return HttpResponse("this is run")