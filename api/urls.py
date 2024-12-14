from django.urls import path
from .views import NoticeViews, UserViews



urlpatterns = [
    path('notices/', NoticeViews.as_view(), name='notice'),
    path('users/', UserViews.as_view(), name='user'),
]
