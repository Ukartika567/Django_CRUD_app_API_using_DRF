from django.urls import path, include
from crudapp.api import views
from rest_framework.routers import DefaultRouter

# Object of DefaultRouter
router=DefaultRouter()


# Register EmployeeViewSet
router.register('crud', views.EmployeeViewSet, basename='employee')

urlpatterns=[
    path('', include(router.urls)),
]