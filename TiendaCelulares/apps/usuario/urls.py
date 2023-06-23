from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.pagina_principal, name='pagina_principal'),
    path('inicio/', views.pagina_principal, name='inicio'),
    path('registro', views.registro, name ="registro"),
    path('acerca/', views.acerca, name='acerca'),
    path('contacto/', views.contacto, name='contacto'),
    path('api/', views.api, name='api'),
    path('producto/', views.producto, name='producto'),
    path('crear', views.ProductoCreate.as_view(), name ="crear"),
    path('editar/<int:pk>/', views.editar.as_view(), name='editar'),
    path('borrar/<int:pk>/', views.borrar, name="borrar"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    

    

