from django.urls import path

from .views import (
    PrivacyPageAPIView,
    PrivacyPageDetailAPIView,
    TermsPageAPIView,
    TermsPageDetailAPIView,
)

urlpatterns = [
    path("terms/", TermsPageAPIView.as_view()),
    path("terms/<int:pk>/", TermsPageDetailAPIView.as_view()),
    path("privacy/", PrivacyPageAPIView.as_view()),
    path("privacy/<int:pk>/", PrivacyPageDetailAPIView.as_view()),
]

