from django.urls import path
from . import views
import myhp
from django.conf.urls import url


app_name = 'myhp' #django2.0以降ではnamespace定義が必要
urlpatterns = [
    #path(r'myhp', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    path('myhp/', myhp.index)
    path('', myhp.index,name='top')
    url(r'^template/$', views.hello_template, name='index'),  # 追加する
    path('<int:question_id>/vote/', views.index(), name='index'),
    #path('', views.index, name='index'),
    #path('', views.news, name='news'), #追加要素
]
