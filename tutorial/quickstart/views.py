from rest_framework import viewsets, permissions
from .serializers import UserSerializer, GroupSerializer
from django.contrib.auth.models import User, Group


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
