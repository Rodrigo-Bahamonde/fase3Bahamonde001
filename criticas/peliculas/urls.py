from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('galeria/', views.galeria, name='galeria'),
    path('endgame/', views.endgame, name='endgame'),
    path('dolittle/', views.dolittle, name='dolittle'),
    path('guerra/', views.guerra, name='guerra'),
    path('joker/', views.joker, name='joker'),

    path('comentario/guerra', views.GuerraListView.as_view(), name='comentarioguerra'),
    path('comentario/guerra/<int:pk>', views.GuerraDetailView.as_view(), name='comentarioguerra-detail'),
    path('comentario/endgame', views.EndgameListView.as_view(), name='comentarioendgame'),
    path('comentario/endgame/<int:pk>', views.EndgameDetailView.as_view(), name='comentarioEndgame-detail'),
    path('comentario/joker', views.JokerListView.as_view(), name='comentariojoker'),
    path('comentario/joker/<int:pk>', views.JokerDetailView.as_view(), name='comentarioJoker-detail'),
    path('comentario/dolittle', views.DolittleListView.as_view(), name='comentariodolittle'),
    path('comentario/dolittle/<int:pk>', views.DolittleDetailView.as_view(), name='comentarioDolittle-detail'),
]

urlpatterns+=[
    path('endgame/create',views.EndgameCreate.as_view(), name='endgame_create'),
    path('endgame/<int:pk>/update',views.EndgameUpdate.as_view(), name='endgame_update'),
    path('endgame/<int:pk>/delete',views.EndgameDelete.as_view(), name='endgame_delete'),
    path('dolittle/create',views.DolittleCreate.as_view(), name='dolittle_create'),
    path('dolittle/<int:pk>/update',views.DolittleUpdate.as_view(), name='dolittle_update'),
    path('dolittle/<int:pk>/delete',views.DolittleDelete.as_view(), name='dolittle_delete'),
    path('guerra/create',views.GuerraCreate.as_view(), name='guerra_create'),
    path('guerra/<int:pk>/update',views.GuerraUpdate.as_view(), name='guerra_update'),
    path('guerra/<int:pk>/delete',views.GuerraDelete.as_view(), name='guerra_delete'),
    path('joker/create',views.JokerCreate.as_view(), name='joker_create'),
    path('joker/<int:pk>/update',views.JokerUpdate.as_view(), name='joker_update'),
    path('joker/<int:pk>/delete',views.JokerDelete.as_view(), name='joker_delete'),
]