from django.urls import path
from . import views

urlpatterns = [
    #Main page
    path('',views.index, name='index'),
    #Ticket search results
    path('search/',views.search, name='search'),
    path('bought/',views.boughtinout, name='boughtinout'),
    path('bought/',views.boughtin, name='boughtin'),
    #Page with map
    path('map/',views.map, name='map'),
    #Map page with results
    path('map/result',views.mapResult, name='mapResult'),
    #User's profile settings page
    path('personal/settings/', views.settings, name="settings"),
    #User's profile page
    path('personal/<int:user_id>/',views.personal, name='personal'),
    #User's flights search result
    path('personal/<int:user_id>/results/',views.personalSearch, name='personalSearch'),
    #Registration page
    path('registration/', views.registerView.as_view(), name="registration"),

    path('logout_view/', views.logout_view, name="logout_view")
]
