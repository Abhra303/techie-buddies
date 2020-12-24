from . import views
from django.urls import path
app_name = 'User'

urlpatterns = [
    path('register/',views.index,name='register'),
    path('login/',views.login1,name='login'),
    path('logout/',views.logout1,name='logout'),
    path('reply/',views.reply,name='reply')
]