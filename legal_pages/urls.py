from django.urls import path

from .views import (
    DisclaimerPageAPIView,
    DisclaimerPageDetailAPIView,
    EditorialPolicyPageAPIView,
    EditorialPolicyPageDetailAPIView,
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
    path("disclaimer/", DisclaimerPageAPIView.as_view()),
    path("disclaimer/<int:pk>/", DisclaimerPageDetailAPIView.as_view()),
    path("editorial-policy/", EditorialPolicyPageAPIView.as_view()),
    path("editorial-policy/<int:pk>/", EditorialPolicyPageDetailAPIView.as_view()),
]

