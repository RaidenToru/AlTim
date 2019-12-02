from django.urls import path
from . import views

app_name = 'AlTim'
urlpatterns = [
    path('',views.index, name='index'),
    path('map/',views.map, name='map'),
    path('personal/',views.personal, name='personal'),
    path('registration/', views.registerView.as_view(), name="registration"),
    path('settings/', views.settingsView, name="settings"),
    path('logout_view/', views.logout_view, name="logout_view"),
]
