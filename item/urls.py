from django.conf.urls import url
from . import views

app_name = 'item'

urlpatterns = [
    #/item/
    url(r'^index/$', views.IndexView.as_view(),name='index'),
    url(r'^$', views.main,name='main'),
    url(r'^register/$', views.UserFormView.as_view(),name='register'),

    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view() , name='detail'),
    #/item/album/add
    url(r'album/add/$',views.AlbumCreate.as_view(), name='album-add'),
    #item/album/2/
    url(r'album/(?P<pk>[0-9]+)/$',views.AlbumUpdate.as_view(), name='album-add'),
    #item/album/2/delete/
    url(r'album/(?P<pk>[0-9]+)/delete/$',views.AlbumDelete.as_view(), name='album-delete'),
]
