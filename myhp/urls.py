from django.urls import path
from . import views

app_name = 'myhp' #django2.0以降ではnamespace定義が必要
urlpatterns = [
    path('', views.index, name='index')
    #path('', views.news, name='news'), #追加要素
]
