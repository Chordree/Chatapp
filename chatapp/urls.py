from . import views
from django.urls import path
# switch imports order ..see what happens 

urlpatterns = [
    path('', views.home, name='homepage'),
    path('base', views.base, name='basepage'),
    path('chat', views.chat, name='chatpage'),
    path('log', views.login, name='loginpage'),
    path('register/', views.register, name='registerpage'),
    path('logout', views.logout, name='logoutpage'),
] 

# todo insatll openAI