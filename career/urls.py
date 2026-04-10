from django.urls import path
from .views import (
    CareerHeroView,
    CareerServiceView,
    CareerSupportView,
    CareerCTAView,
    FAQView,
    CareerPageView,
    MetaTagsAPI,
    MetaTagsDetailAPI,
    CareerServicesHeadingView,
)

urlpatterns = [

    # 🔷 HERO
    path('hero/', CareerHeroView.as_view()),
    path('hero/<int:pk>/', CareerHeroView.as_view()),

    # 🔷 SERVICES (Single + Bulk delete supported)
    path('services/', CareerServiceView.as_view()),
    path('services/<int:pk>/', CareerServiceView.as_view()),

    # 🔷 SERVICES SECTION HEADING (singleton)
    path('services-heading/', CareerServicesHeadingView.as_view()),
    path('services-heading/<int:pk>/', CareerServicesHeadingView.as_view()),

    # 🔷 CAREER SUPPORT
    path('support/', CareerSupportView.as_view()),
    path('support/<int:pk>/', CareerSupportView.as_view()),

    # 🔷 CTA
    path('cta/', CareerCTAView.as_view()),
    path('cta/<int:pk>/', CareerCTAView.as_view()),

    # 🔷 FAQ (Single + Bulk delete)
    path('faqs/', FAQView.as_view()),
    path('faqs/<int:pk>/', FAQView.as_view()),

    # 🔥 MAIN PAGE API (use this in frontend)
    path('page/', CareerPageView.as_view()),

    # 🔷 META TAGS
    path("meta-tags/", MetaTagsAPI.as_view()),
    path("meta-tags/<int:pk>/", MetaTagsDetailAPI.as_view()),
]