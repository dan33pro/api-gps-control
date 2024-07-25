from django.urls import path, include
from rest_framework import routers
from interesteds import views

router = routers.DefaultRouter()
router.register(r'interesteds', views.InterestedViewSet)

urlpatterns = [
    path('', include(router.urls))
]