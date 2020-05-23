from django.conf.urls import url
from django.urls import path
from .dynamic_views import *
urlpatterns = [
	path('stage1', stage1, name='stage1_view'),
	path('stage2', stage2, name='stage2_view'),
	path('stage3', stage3, name='stage3_view'),
	path('stage4', stage4, name='stage4_view'),
]
