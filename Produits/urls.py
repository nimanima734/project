from django.urls import path
from .views import * 
from django.conf import settings
from django.conf.urls.static import static
from Utilisateurs.views import * 
from django.views.generic import TemplateView


urlpatterns = [
 


    path('about/', TemplateView.as_view(template_name="about.html"), name='about'),

    path('products/', Affichage.as_view(), name='products'),
    path('ajout/', AjoutProduits.as_view(), name='add'),
    # path('modification/<int:id>/', modifier,name='modifier'),

    path('modication/<int:pk>/', update_donnees.as_view(), name='modifier'),
    # path('supprimer/<int:id>/', supprimer, name="supprimer"),
#    path ('detail/<int:id>/', detail,name='detail'),
    path('detail/<int:pk>/', edit.as_view(),name='detail'),
    
    path('delete/<int:id>/', delete_product,name='delete'),

    path('recherche/', recherche, name='recherche'),
    path('filter/', Filter, name='filter'),
    path('ajoutvente/<int:id>/', VenteProduits, name='ajoutvente'),
    path('saverecu/<int:id>/', SaveRecu, name='saverecu'),
    path('facture/<int:sale_id>/', Facture, name='facture'),
    # path('ajout/',ajout_donnees,name='ajout'),

   
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



