from .models import UserProfile
from rest_framework import viewsets, permissions
from .serializers import UserProfileSerializer


class UserProfileViewset(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return self.request.user.profiles.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
