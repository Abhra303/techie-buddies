from . import views
from django.urls import path
app_name='Blog'

urlpatterns = [
    path('',views.index,name="news"),
    path('tags/<slug:value>',views.tagindex),
    path('post/<int:val>',views.post,name='post'),
    path('<slug:name>',views.tagpost,name='tagpost'),
    path('page/<int:index>',views.index),
    
    path('<slug:name>/page/<int:index>',views.tagpost)
]