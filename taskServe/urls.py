from rest_framework import routers

from taskServe import views

router = routers.DefaultRouter()
router.register(r'tasks', views.TaskViewSet)
router.register(r'calendars', views.CalendarViewSet)

urlpatterns = router.urls
