from django.contrib import admin

from articles.models import Libreria
from articles.models import Papeleria
from articles.models import Artistica

""" admin.site.register(Libreria)
admin.site.register(Papeleria)
admin.site.register(Artistica) """

@admin.register(Libreria)
class Libreria_admin(admin.ModelAdmin):
    list_display = ['name','price','description','active']

@admin.register(Papeleria)
class Libreria_admin(admin.ModelAdmin):
    list_display = ['name','price','description','active']

@admin.register(Artistica)
class Libreria_admin(admin.ModelAdmin):
    list_display = ['name','price','description','active']