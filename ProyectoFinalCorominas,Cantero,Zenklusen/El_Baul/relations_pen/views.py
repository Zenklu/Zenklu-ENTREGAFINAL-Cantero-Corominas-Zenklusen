from django.shortcuts import render
from django.http import HttpResponse

from relations_pen.models import Pen_style



def pen_relations(request):

    styles = Pen_style.objects.all()
    for style in styles:
        print(style.name)
        print(style.style_pen.all())

    return HttpResponse ('prueba')
    

