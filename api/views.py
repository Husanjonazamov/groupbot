from django.shortcuts import render
from rest_framework.generics import ListAPIView
from main.models import Notice, User
from .serializers import NoticeSerializers, UserSerializers



class NoticeViews(ListAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializers
    
    
    

class UserViews(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers