from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index,name="index"),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('add/',views.add,name='add'),
    path('detailview/<str:pk>/',views.detailview,name='detailview'),
    path('user_logout/',views.user_logout,name='user_logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('Home',views.Home.as_view(),name='Home'),


]
