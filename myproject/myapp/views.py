from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context


def BASE(request):
      return render (request, 'planilla1.html')