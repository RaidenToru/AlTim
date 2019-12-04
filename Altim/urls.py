from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('map/',views.map, name='map'),
    path('map/result',views.mapResult, name='mapResult'),
    path('settings/', views.settingsView, name="settings"),
    path('personal/<int:user_id>/',views.personal, name='personal'),
    path('personal/<int:user_id>/results/',views.personalSearch, name='personalSearch'),
    path('registration/', views.registerView.as_view(), name="registration"),
    path('logout_view/', views.logout_view, name="logout_view")
]
