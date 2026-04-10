from django.urls import path
from .views import *

urlpatterns = [

    # HERO
    path("hero/", HeroAPI.as_view()),
    path("hero/<int:pk>/", HeroDetailAPI.as_view()),

    # FEATURES
    path("features/", FeatureAPI.as_view()),
    path("features/<int:pk>/", FeatureDetailAPI.as_view()),
    path("features/bulk-create/", FeatureBulkCreateAPI.as_view()),
    path("features/bulk-delete/", FeatureBulkDeleteAPI.as_view()),

    # CTA
    path("cta/", CTAAPI.as_view()),
    path("cta/<int:pk>/", CTADetailAPI.as_view()),

    # FORM
    path("form/", FormAPI.as_view()),
    path("form/<int:pk>/", FormDetailAPI.as_view()),

    path("instructor-page/", InstructorPageAPI.as_view()),
    path("applications/submit/", InstructorApplicationSubmitAPI.as_view()),
    path("applications/", InstructorApplicationListAPI.as_view()),
    path("applications/<int:pk>/", InstructorApplicationDetailAPI.as_view()),
]