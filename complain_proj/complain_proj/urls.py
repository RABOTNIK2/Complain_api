"""
URL configuration for complain_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from complain_app import views as complain_api
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'category', complain_api.CategoryViewSet)
router.register(r'user', complain_api.UserViewSet)
router.register(r'complain', complain_api.ComplainViewSet)
router.register(r'answer', complain_api.AnswerViewSet, basename='answer')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('complain_api/', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
