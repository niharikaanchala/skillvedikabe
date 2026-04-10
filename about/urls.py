from django.urls import path

from .views import (
    AboutContentAPIView,
    AboutHeroAPIView,
    CtaSectionAPIView,
    DemoSectionAPIView,
    ValueItemAPIView,
    ValuesSectionAPIView,
    MetaTagsAPI,
    MetaTagsDetailAPI,
)

urlpatterns = [
    path("", AboutContentAPIView.as_view(), name="about-content"),

    # META TAGS (SEO)
    path("meta-tags/", MetaTagsAPI.as_view(), name="about-meta-tags"),
    path("meta-tags/<int:pk>/", MetaTagsDetailAPI.as_view(), name="about-meta-tags-detail"),

    path("hero/", AboutHeroAPIView.as_view(), name="about-hero-list"),
    path("hero/<int:pk>/", AboutHeroAPIView.as_view(), name="about-hero-detail"),
    path("values-section/", ValuesSectionAPIView.as_view(), name="about-values-section-list"),
    path("values-section/<int:pk>/", ValuesSectionAPIView.as_view(), name="about-values-section-detail"),
    path("values/", ValueItemAPIView.as_view(), name="about-values-list"),
    path("values/<int:pk>/", ValueItemAPIView.as_view(), name="about-values-detail"),
    path("cta/", CtaSectionAPIView.as_view(), name="about-cta-list"),
    path("cta/<int:pk>/", CtaSectionAPIView.as_view(), name="about-cta-detail"),
    path("demo/", DemoSectionAPIView.as_view(), name="about-demo-list"),
    path("demo/<int:pk>/", DemoSectionAPIView.as_view(), name="about-demo-detail"),
]
