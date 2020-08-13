from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    #! FUNCTION BASE VIEWS
    path('article/', views.article_list, name='article_list'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),

    #! CLASS BASE VIEWS
    path('', views.IndexAPIView.as_view(), name='article_list_index_class'),
    path('articleclass/', views.ArticleAPIView.as_view(), name='article_list_class'),
    path('articleclass/<int:article_id>/', views.ArticleDetailsAPIView.as_view(), name='article_detail_class')
]