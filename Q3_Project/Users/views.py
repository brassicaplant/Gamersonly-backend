from rest_framework import generics

from .models import Users
from .serializers import UsersSerializer
# Create your views here.

class UsersListCreate(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

