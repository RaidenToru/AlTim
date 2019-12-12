from django.urls import path
from . import views

urlpatterns = [
    #Main page
    path('',views.index, name='index'),
    #Ticket search results
    path('search/',views.search, name='search'),
    #Message of bought page
    path('bought/',views.bought, name='bought'),
    #Reviews page
    path('review/<int:flight_id>',views.review, name='review'),
    #Review add Page
    path('personal/reviewAdd/<int:plane_id>',views.reviewAdd, name='reviewAdd'),
    #Page with map
    path('map/',views.map, name='map'),
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
