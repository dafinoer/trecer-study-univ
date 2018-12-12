from django.urls import path

from . import views

urlpatterns = [
    # path('')
    path('login/', views.login, name='login-view-user'),
    path('logout/', views.logout_view, name='logout-view-user')
]