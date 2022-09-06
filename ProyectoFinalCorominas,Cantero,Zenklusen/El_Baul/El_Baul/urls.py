
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
from relations_pen.views import pen_relations

from articles.views import pagina_principal,nuestro_proyecto,all_articles_list, search_article \
    ,create_libreria, list_libreria, detail_libreria, manage_libreria, update_libreria, delete_libreria \
    ,create_papeleria, list_papeleria,detail_papeleria, manage_papeleria,update_papeleria, delete_papeleria \
    ,Create_artistica,List_artistica,Detail_artistica,Manage_artistica,Delete_artistica,Update_artistica


urlpatterns = [
    path('admin/', admin.site.urls),

    path ('',pagina_principal, name='pagina_principal'),
    path ('pagina-principal/',pagina_principal,name='pagina_principal' ),
    
    #URLs Libreria
    path ('nueva-libreria/', create_libreria, name='create_libreria'),
    path ('lista-libreria/', list_libreria, name='list_libreria'),
    path ('detalle-libreria/<int:pk>/',detail_libreria, name='detail_libreria'),
    path ('gestor-libreria/',manage_libreria, name='manage_libreria'),
    path ('eliminar-libreria/<int:pk>/',delete_libreria, name='delete_libreria'),
    path ('actualizar-libreria/<int:pk>/',update_libreria, name='update_libreria'),

    #URLs Artistica
    path ('nueva-artistica/', Create_artistica.as_view(), name='Create_artistica'),# Al usar class se agrega el .as_view
    path ('lista-artistica/', List_artistica.as_view(), name='Lista_artistica'),
    path ('detalle-artistica/<int:pk>/', Detail_artistica.as_view(), name='Detail_artistica'),
    path('gestor-artistica/',Manage_artistica.as_view(), name='Manage_artistica' ),
    path('eliminar-artistica/<int:pk>/',Delete_artistica.as_view(), name='Delete_artistica' ),
    path('actualizar-artistica/<int:pk>/',Update_artistica.as_view(), name='Update_artistica' ),

    #URLs Papeleria
    path ('nueva-papeleria/', create_papeleria, name='create_papeleria'),
    path ('lista-papeleria/', list_papeleria, name='list_papeleria'),
    path ('detalle-papeleria/<int:pk>/',detail_papeleria, name='detail_papeleria'),
    path('gestor-papeleria/',manage_papeleria, name='manage_papeleria'),
    path ('eliminar-papeleria/<int:pk>/',delete_papeleria, name='delete_papeleria'),
    path('actualizar-papeleria/<int:pk>/',update_papeleria, name='update_papeleria'),
    

    path ('relacion-lapices/',pen_relations , name='pen_relations '),
    path ('search-article/',search_article, name='search_article'),
    path ('todos-articulos/',all_articles_list, name='all_articles_list'),
    path ('nuestro-proyecto/',nuestro_proyecto, name='nuestro_proyecto'),

    #Users
    path ('users/', include('users.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
