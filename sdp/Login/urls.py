from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^signin', views.index2, name='index2'),    
    url(r'^$', views.index, name='index'),
    url(r'^loginn/$',views.LoginRequest.as_view(),name="login"),
    url(r'^(?P<pk>[0-9]+)/$',views.UpdateProfile.as_view(),name="update")

]

