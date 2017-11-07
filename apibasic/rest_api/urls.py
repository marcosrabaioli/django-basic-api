from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^farms/$', views.FarmsList.as_view(), name='farms-list'),

    url(r'^example/$', views.ExampleList.as_view(), name='example-list')

]