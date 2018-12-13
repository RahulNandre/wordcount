from django.urls import path
from . import views
urlpatterns = [
    path('',views.homepage,name='home'),
    path('eggs/',views.eggs),
    path('countthewords/',views.count,name='count'),
    path('about/',views.about,name='about')
]
