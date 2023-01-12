"""Pokemon_Remember URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from users.views import UserViewSet

#access토큰이 잘 작동하는지 확인하기 위한 API를 rest_framework에 내장돼있는 Router 기능을 사용해 간단히 만듦.
router = routers.DefaultRouter()
router.register('userss', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    #회원가입/로그인
    path('users/', include('dj_rest_auth.urls')),
    path('users/registration/', include('dj_rest_auth.registration.urls')),
    path('users/', include('allauth.urls')),
    #앱
    path('users/', include('users.urls')),
    #path('users/pokemons/', include('pokemons.urls')),
]
