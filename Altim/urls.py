from django.urls import path
from . import views

app_name = 'AlTim'
urlpatterns = [
    path('',views.index, name='index'),
    path('map/',views.map, name='map'),
<<<<<<< HEAD
    path('personal/',views.personal, name='personal'),
    path('registration/', views.registerView.as_view(), name="registration"),
    path('settings/', views.settingsView, name="settings"),
    path('logout_view/', views.logout_view, name="logout_view"),
=======
    path('personal/<int:user_id>/',views.personal, name='personal'),
    path('personal/<user_id>/results/',views.get_search_result, name='get_search_result')
>>>>>>> db1f09bc7a6896f6558f7e14562e2285701a49d8
]
