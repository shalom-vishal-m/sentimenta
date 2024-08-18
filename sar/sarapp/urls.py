from django.urls import path
from .views import analyze,result

urlpatterns = [
       path('', analyze, name='analyze'),
      
       path('result/<int:pk>/', result, name='result'),
   ]
