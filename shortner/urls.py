from django.urls import path
from .views import home, makeurl, redirect

urlpatterns = [
    path('', home),
    path('makeurl/', makeurl, name='makeurl'),
    path('<url>/', redirect)
    
]
