from django.urls import path
from . import views

app_name = 'AlTim'
urlpatterns = [
    path('',views.index, name='index'),
    path('map/',views.map, name='map'),
    path('map/result',views.mapResult, name='mapResult'),
    path('personal/<int:user_id>/',views.personal, name='personal'),
    path('personal/<user_id>/results/',views.get_search_result, name='get_search_result'),
    path('registration/', views.registerView.as_view(), name="registration"),
    path('settings/', views.settingsView, name="settings"),
    path('logout_view/', views.logout_view, name="logout_view"),
]
