

from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render

from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView #Realizaciones automaticas aplicadas en el Model Artistica

from articles.models import Libreria
from articles.models import Artistica
from articles.models import Papeleria
from articles.forms import Formulario_articulo


from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


#BUSCADOR
def search_article(request): #Busqueda general en todas las categorías
    
    search=request.GET['search']
    article_1= Libreria.objects.filter(name__icontains=search)
    article_2= Papeleria.objects.filter(name__icontains=search)
    article_3= Artistica.objects.filter(name__icontains=search)
    context={
        'article_1':article_1,
        'article_2':article_2,
        'article_3':article_3

    }
    return render(request, 'search_article.html',context=context)

def all_articles_list(request):
    article_1= Libreria.objects.all()
    article_2= Papeleria.objects.all()
    article_3= Artistica.objects.all()
    context={
        'article_1':article_1,
        'article_2':article_2,
        'article_3':article_3
    }
    return render(request, 'all_articles_list.html',context=context)


#LIBRERIA MODEL
@login_required #requerimiento de logueo
def create_libreria(request): #Formulario para crear artículo en libreria y devolverlo en lista
    if request.user.is_superuser:  #requerimiento de ser admin   
        if request.method=='POST':
            form = Formulario_articulo(request.POST, request.FILES)
            
            if form.is_valid():
                Libreria.objects.create(
                    name=form.cleaned_data['name'],
                    price=form.cleaned_data['price'],
                    description = form.cleaned_data['description'],
                    image = form.cleaned_data ['image']
                )
                return redirect(list_libreria)
            
        elif request.method =='GET':
            form = Formulario_articulo()
            context = {'form': form}
            return render(request,'librerias/create_libreria.html', context=context)
    else:
        return HttpResponse("No tiene permisos para realizar esta acción")    

def list_libreria(request): #lista de objetos en libreria
    librerias = Libreria.objects.all()
    context={
        'librerias': librerias
    }
    return render(request, 'librerias/librerias_list.html', context=context)

@login_required
def detail_libreria(request,pk):
    if request.method =='GET':
        libreria = Libreria.objects.get(id=pk)
        context ={
                'name':libreria.name,
                'price':libreria.price,
                'description':libreria.description}
        
        return render (request, 'librerias/detail_libreria.html',context=context)

@login_required
def manage_libreria(request): #lista de objetos en libreria
    if request.user.is_superuser:    
        librerias = Libreria.objects.all()
        context={
            'librerias': librerias
        }
        return render(request, 'librerias/manage_libreria.html', context=context)
    else:
        return HttpResponse("No tiene permisos para realizar esta acción")    

@login_required    
def update_libreria(request,pk):
    if request.user.is_superuser:       
        if request.method == 'POST':
            form = Formulario_articulo(request.POST, request.FILES)
            if form.is_valid():
                
                libreria= Libreria.objects.get(id=pk)               
                libreria.name=form.cleaned_data['name']
                libreria.price=form.cleaned_data['price']
                libreria.description = form.cleaned_data['description']
                libreria.image = form.cleaned_data['image']
                libreria.save()

            return redirect(list_libreria)

        elif request.method == 'GET':
            libreria = Libreria.objects.get(id=pk)

            form = Formulario_articulo(initial ={
                    'name':libreria.name,
                    'price':libreria.price,
                    'description':libreria.description,
                    'image':libreria.image
                    })
            context ={'form' : form}
            return render (request, 'librerias/update_libreria.html',context=context)
    else:
        return HttpResponse("No tiene permisos para realizar esta acción")    

@login_required
def delete_libreria (request,pk): #pk es lo mismo que id
    if request.user.is_superuser:
        if request.method == 'GET':
            libreria = Libreria.objects.get(pk=pk)
            context ={'libreria':libreria}
            return render ( request, 'librerias/delete_libreria.html', context=context)
        elif request.method == 'POST':
            libreria = Libreria.objects.get(pk=pk)
            libreria.delete()
            return redirect(list_libreria)
    else:
        return HttpResponse("No tiene permisos para realizar esta acción")    


#PAPELERIA MODEL
def create_papeleria(request): #Formulario para crear artículo en papeleria y devolverlo en lista
    if request.user.is_superuser:
        if request.method=='POST':
            form = Formulario_articulo(request.POST, request.FILES)
            
            if form.is_valid():
                Papeleria.objects.create(
                    name=form.cleaned_data['name'],
                    price=form.cleaned_data['price'],
                    description = form.cleaned_data['description'],
                    image = form.cleaned_data ['image']
                )
                return redirect(list_papeleria)
            
        elif request.method =='GET':
            form = Formulario_articulo()
            context = {'form': form}
            return render(request,'papelerias/create_papelerias.html', context=context)
    else:
        return HttpResponse("No tiene permisos para realizar esta acción")    

def list_papeleria(request):

    papelerias = Papeleria.objects.all()
    context={
        'papelerias': papelerias
    }
    return render(request, 'papelerias/papelerias_list.html', context=context)

@login_required
def detail_papeleria(request,pk):
    if request.method =='GET':
        papeleria = Papeleria.objects.get(id=pk)
        context ={
                'name':papeleria.name,
                'price':papeleria.price,
                'description':papeleria.description}
        
        return render (request, 'papelerias/detail_papeleria.html',context=context)

@login_required
def manage_papeleria(request):
    if request.user.is_superuser:
        papelerias = Papeleria.objects.all()
        context={
            'papelerias': papelerias
        }
        return render(request, 'papelerias/manage_papeleria.html', context=context)
    else:
        return HttpResponse("No tiene permisos para realizar esta acción")    

@login_required
def update_papeleria(request,pk):
    if request.user.is_superuser:    
        if request.method == 'POST':
            form = Formulario_articulo(request.POST)
            if form.is_valid():
                papeleria= Papeleria.objects.get(id=pk)
                papeleria.name=form.cleaned_data['name']
                papeleria.price=form.cleaned_data['price']
                papeleria.description = form.cleaned_data['description']
                papeleria.save()

                return redirect(list_papeleria)

        elif request.method == 'GET':
            papeleria = Papeleria.objects.get(id=pk)

            form = Formulario_articulo(initial ={
                    'name':papeleria.name,
                    'price':papeleria.price,
                    'description':papeleria.description})
            context ={'form' : form}
            return render (request, 'papelerias/update_papelerias.html',context=context)
    else:
        return HttpResponse("No tiene permisos para realizar esta acción")    
    
@login_required
def delete_papeleria (request,pk): #pk es lo mismo que id
    if request.user.is_superuser:    
        if request.method == 'GET':
            papeleria = Papeleria.objects.get(pk=pk)
            context ={'papeleria':papeleria}
            return render ( request, 'papelerias/delete_papeleria.html', context=context)
        elif request.method == 'POST':
            papeleria = Papeleria.objects.get(pk=pk)
            papeleria.delete()
            return redirect(list_papeleria)
    else:
        return HttpResponse("No tiene permisos para realizar esta acción")    


#ARTISTICA MODEL
 
class Create_artistica(LoginRequiredMixin,CreateView):

    model= Artistica
    template_name = 'artisticas/create_artistica.html'
    fields= '__all__' #para agregar todos los campos
    success_url= '/list-artistica/'


class List_artistica(ListView):

    model = Artistica
    template_name= 'artisticas/artisticas_list.html'


class Detail_artistica(LoginRequiredMixin,DetailView):
    model =Artistica
    template_name = 'artisticas/detail_artistica.html'


class Manage_artistica(LoginRequiredMixin,ListView):
    model= Artistica
    template_name = 'artisticas/manage_artistica.html'


class Delete_artistica(LoginRequiredMixin,DeleteView):
    model= Artistica
    template_name = 'artisticas/delete_artistica.html'
    success_url= '/list-artistica/'

class Update_artistica(LoginRequiredMixin,UpdateView):
    model = Artistica
    fields= '__all__'
    template_name= 'artisticas/act_artistica.html'
    success_url = '/lista-artistica/'

#PAGINA PRINCIPAL
def pagina_principal (request):
    return render(request,'principal/principal.html', context={})

def nuestro_proyecto (request):
    return render(request,'nuestro_proyecto/viewme.html', context={})
