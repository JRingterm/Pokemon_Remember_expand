from django.urls import path, include
from rest_framework import routers
from users.views import UserViewSet

#access토큰이 잘 작동하는지 확인하기 위한 API를 rest_framework에 내장돼있는 Router 기능을 사용해 간단히 만듦.
router = routers.DefaultRouter()
router.register('userss', UserViewSet)

urlpatterns = [
   path('', include(router.urls)),
]