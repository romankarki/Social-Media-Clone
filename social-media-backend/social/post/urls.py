from rest_framework import routers
from .api import PostViewset

router = routers.DefaultRouter()

router.register('api/post', PostViewset, 'posts')

urlpatterns = router.urls
