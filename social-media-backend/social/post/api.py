from .models import Post
from rest_framework import viewsets, permissions
from .serializers import PostSerializer
from user_profile.models import UserProfile


class PostViewset(viewsets.ModelViewSet):

    permission_classes = [
        permissions.IsAuthenticated,
    ]

    serializer_class = PostSerializer

    queryset = Post.objects.all()

    def perform_create(self, serializer):
        q = UserProfile.objects.get(user=self.request.user)
        serializer.save(user=self.request.user)
        serializer.save(username=q.name)
