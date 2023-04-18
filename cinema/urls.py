
from django.urls import path
from . import views

app_name = 'cinema'

urlpatterns = [
    path('', views.cine, name='index'),
    path('news/', views.news, name='news'),
    path('films/', views.films, name='films'),
    path('reservations/', views.reservations, name='reservations'),
    # path(r'^films/(?P<pk>\d+)$', views.FilmsDetailView.as_view(), name='filmsDetail'),
    # path('films/<int:pk>', views.FilmsDetailView.as_view(), name='filmsDetail'),
    path('films/<int:idfilm>', views.filmsDetail, name='filmDetail'),
]