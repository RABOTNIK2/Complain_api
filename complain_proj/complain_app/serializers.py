from .models import *
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'home_adress']
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        
class ComplainSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    written_by = serializers.StringRelatedField()
    class Meta:
        model = Complain
        fields = '__all__'
        
class AnswerSerializer(serializers.ModelSerializer):
    answer_to_compl = serializers.StringRelatedField()
    class Meta:
        model = Answer
        fields = '__all__'