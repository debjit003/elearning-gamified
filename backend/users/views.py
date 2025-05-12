from django.shortcuts import render

# users/views.py

from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

# Register View
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

# Profile View
class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


