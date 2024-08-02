from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, views, permissions, status
from .models import CustomUser
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from django.shortcuts import redirect
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from .permissions import IsTeamOwner
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.tokens import RefreshToken
class UserDetailView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            serializer = UserSerializer(request.user)
            return Response(serializer.data)
        login_url = "/api-auth/login/"
        return redirect(login_url)
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    def get_permissions(self):
        if self.action == "list":
            permission_classes = [permissions.IsAuthenticated]
        elif self.action in "create":
            permission_classes = [permissions.AllowAny]
        elif self.action in ["update", "partial_update"]:
            permission_classes = [IsTeamOwner]
        elif self.action == "destroy":
            ermission_classes = [IsTeamOwner]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]
class UserLogoutView(views.APIView):
    def post(self, request, *args, **kwargs):
# Expire JWT token
        if request.user.is_authenticated:
            try:
                refresh_token = request.COOKIES['access_token']
                RefreshToken(refresh_token).blacklist()
                return Response({"message": "Successfully logged out."},status=status.HTTP_200_OK)
            except KeyError:
                return Response({"error": "'refresh_token' cookie notfound."}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "User not authenticated."},status=status.HTTP_401_UNAUTHORIZED)