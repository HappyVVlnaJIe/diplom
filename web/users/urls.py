from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('', views.root_view, name='root_view'),
    path('profile',views.profile_view,name='profile_view'),
    path('business_trip',views.business_trip_view,name='business_trip_view'),
    path('documents',views.documents_view,name='documents_view'),
    path('accounts/register/', views.registration, name="register"),
    url('^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate,
        name='activate'),
    path('settings', views.edit, name='edit'),
]