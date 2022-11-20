from django.urls import path
from core import views
from django.views.generic import RedirectView 
urlpatterns = (
    path('index/', views.index, name='index'),
    path('', RedirectView.as_view(url='index')),
    path('login/', views.login_user, name='login'),
    path('register', views.register_user, name='register'),
    path('novo_evento/', views.new_event, name='evento_novo'),
    path('<int:id_evento>/delete', views.delete_evento, name='delete'),
    path("novo_evento/<int:id>", views.new_event, name="detalhes"),
    path('login/submit', views.submit_login),
    path('logout', views.logout_user, name='logout'),

)