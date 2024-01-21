from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('uploadPage',views.uploadPage,name='uploadPage'),
    path('upload',views.upload,name='upload'),
    path('download/<str:Filename>',views.download,name='download'),
]