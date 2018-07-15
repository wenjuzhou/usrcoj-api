from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from user import views

router = DefaultRouter()
router.register(r'', views.UserViewSet)

urlpatterns = [
    url(r'', include(router.urls))
]
