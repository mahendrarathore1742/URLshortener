from django.urls import path

from .views import signup,loginuser,logoutuser
urlpatterns = [
    
     path("account/signup/",signup,name="signup"),
     path('account/login/',loginuser,name='login'),
     path("account/logout/",logoutuser,name='logout')
]
  
