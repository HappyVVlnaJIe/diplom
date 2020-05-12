from django.urls import path
from . import views

urlpatterns = [
    path('', views.root_view, name='root_view'),
    path('profile',views.profile_view,name='profile_view'),
    path('business_trip',views.business_trip_view,name='business_trip_view'),
    path('documents',views.documents_view,name='documents_view'),
]