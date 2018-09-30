from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
# Create your views here.

app_name='blog'

def blog(request):
     template = loader.get_template('blog.html')
     return HttpResponse(template.render({},request))