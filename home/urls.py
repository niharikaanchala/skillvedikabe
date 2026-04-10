from django.urls import path
from .views import (
    HeroView,
    FeatureView,
    FeatureDetailView,
    WhyChooseView,
    WhyChooseDetailView,
    JobProgramView,
    JobProgramDetailView,
    FAQView,
    FAQDetailView,
    HomePageBundleView,
    SupportSectionView,
    SectionCopyView,
    SectionCopyDetailView,
    SiteBrandingView,
)

urlpatterns = [
    path("bundle/", HomePageBundleView.as_view(), name="home_bundle"),
    path("hero/", HeroView.as_view(), name="hero"),
    path("features/", FeatureView.as_view(), name="features"),
    path("features/<int:pk>/", FeatureDetailView.as_view(), name="feature_detail"),
    path("why-choose/", WhyChooseView.as_view(), name="why_choose"),
    path("why-choose/<int:pk>/", WhyChooseDetailView.as_view(), name="why_choose_detail"),
    path("job-program/", JobProgramView.as_view(), name="job_program"),
    path("job-program/<int:pk>/", JobProgramDetailView.as_view(), name="job_program_detail"),
    path("faq/", FAQView.as_view(), name="faq"),
    path("faq/<int:pk>/", FAQDetailView.as_view(), name="faq_detail"),
    path("support/", SupportSectionView.as_view(), name="support"),
    path("branding/", SiteBrandingView.as_view(), name="branding"),
    path("section-copy/", SectionCopyView.as_view(), name="section_copy_list"),
    path("section-copy/<str:section>/", SectionCopyDetailView.as_view(), name="section_copy_detail"),
]
