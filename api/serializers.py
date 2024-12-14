from main.models import Notice, User
from rest_framework.serializers import ModelSerializer





class NoticeSerializers(ModelSerializer):
    class Meta:
        model = Notice
        fields = '__all__'


class UserSerializers(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'