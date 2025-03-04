from django.urls import include, path
from rest_framework.routers import DefaultRouter

from program.viewsets import ProposalViewSet

session_router = DefaultRouter()
session_router.register("sessions", ProposalViewSet, basename="session")

urlpatterns = [
    path("", include(session_router.urls)),     # TODO: 이전됨 -> FE 수정 후 삭제 예정
]
