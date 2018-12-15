from django.urls import path
from . import views

app_name = 'problems'
urlpatterns = [
    path('<int:problem_id>/', views.Detail.as_view(), name='detail'),
    path('ctf/<str:ctf>/', views.Index.as_view(), name='ctf'),
    path('category/<str:cate>/', views.CIndex.as_view(), name='category'),

]
