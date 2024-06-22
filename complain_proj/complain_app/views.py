from django.shortcuts import render
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework import permissions
from .permissions import AnswerPermissions

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    @action(detail=False, methods=['POST'])
    def get_complains(self, request):
        query = request.data['id']
        if query is None:
            return Response({'message':'Ошибка ничего не найдено'}, status=status.HTTP_404_NOT_FOUND)
        complain = Complain.objects.filter(written_by=query)
        serializer = ComplainSerializer(complain, many=True)
        return Response(serializer.data)
    
class ComplainViewSet(viewsets.ModelViewSet):
    queryset = Complain.objects.all()
    serializer_class = ComplainSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class AnswerViewSet(viewsets.ViewSet):
    permission_classes = [AnswerPermissions]
    
    def list(self, request):
        queryset = Answer.objects.all()
        serializer = AnswerSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def retrieve(self, request, pk=None):
        try:
            answer = Answer.objects.get(pk=pk)
            serializer = AnswerSerializer(answer)
            return Response(serializer.data)
        except Answer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        try:
            answer = Answer.objects.get(pk=pk)
            serializer = AnswerSerializer(answer, request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        except Answer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            answer = Answer.objects.get(pk=pk)
            answer.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Answer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
# Create your views here.
