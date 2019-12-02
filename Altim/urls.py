from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('map/',views.map, name='map'),
    path('personal/<int:user_id>/',views.personal, name='personal'),
    path('personal/<user_id>/results/',views.get_search_result, name='get_search_result')
]
