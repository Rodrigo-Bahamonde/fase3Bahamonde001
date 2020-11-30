from django.urls import path
from . import views
from django.urls import include

urlpatterns=[
    path('signup/', views.RegistroUsuario.as_view(), name='signup'),
    path('perfil/', views.perfil, name='perfil'),
]

urlpatterns+=[
    path('perfil/<str:pk>/update',views.UsuarioUpdate.as_view(), name='perfil_update'),
    path('perfil/<str:pk>/delete',views.UsuarioDelete.as_view(), name='perfil_delete'),
    path('usuarios/',views.UsuarioListView.as_view(), name='usuario_list'),
]