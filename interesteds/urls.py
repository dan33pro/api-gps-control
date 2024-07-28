from django.urls import path, include
from rest_framework import routers
from interesteds import views

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('interesteds/', views.interested_list_create, name='interested-list-create'),
    path('interesteds/<int:pk>/', views.interested_detail, name='interested-detail'),
]
