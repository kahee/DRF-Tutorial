from django.urls import path
from . import views

app_name = 'snippets'
urlpatterns = [

    path('', views.SnippetList.as_view(), name='snippets-list'),
    path('<int:pk>/', views.SnippetDetail.as_view(), name="snippets-detail"),

]
