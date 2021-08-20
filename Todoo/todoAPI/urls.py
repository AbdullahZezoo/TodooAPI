from django.urls import path, include
from rest_framework import routers
from .views import TaskView, finish_task, filter_tasks


router = routers.DefaultRouter()
router.register(r'tasks', TaskView)

urlpatterns = [
    path('', include(router.urls)),
    path('finish_task/<id>', finish_task),
    path('filter_tasks/<str:type>', filter_tasks)
]
