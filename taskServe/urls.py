from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from taskServe import views

router = routers.DefaultRouter()
router.register(r'tasks', views.TaskViewSet)
router.register(r'calendars', views.CalendarViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token)
]
