from rest_framework import routers
from .api import UserProfileViewset

router = routers.DefaultRouter()

router.register('api/userprofile',UserProfileViewset,'user-profile')

urlpatterns = router.urls

