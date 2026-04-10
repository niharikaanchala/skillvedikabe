from django.urls import path
from .views import *

urlpatterns = [
    # ✅ Course
    path("course/<str:slug>/", CourseDetailView.as_view()),
    path("course/<str:slug>/meta/", CourseSectionMetaView.as_view()),

    # ✅ Sections (ALL USING SLUG)
    path("course/<str:slug>/about/", AboutView.as_view()),
    path("course/<str:slug>/about/<int:pk>/", AboutView.as_view()),
    path("course/<str:slug>/skills/", SkillView.as_view()),
    path("course/<str:slug>/skills/<int:pk>/", SkillView.as_view()),
    path("course/<str:slug>/tools/", ToolView.as_view()),
    path("course/<str:slug>/tools/<int:pk>/", ToolView.as_view()),
    path("course/<str:slug>/curriculum/", CurriculumView.as_view()),
    path("course/<str:slug>/curriculum/<int:pk>/", CurriculumView.as_view()),
    path("course/<str:slug>/projects/", ProjectView.as_view()),
    path("course/<str:slug>/projects/<int:pk>/", ProjectView.as_view()),
    path("course/<str:slug>/salary/", SalaryView.as_view()),
    path("course/<str:slug>/salary/<int:pk>/", SalaryView.as_view()),
    path("course/<str:slug>/placement-support/", PlacementSupportView.as_view()),
    path("course/<str:slug>/placement-support/<int:pk>/", PlacementSupportView.as_view()),
    path("course/<str:slug>/corporate-training/", CorporateTrainingView.as_view()),
    path("course/<str:slug>/corporate-training/<int:pk>/", CorporateTrainingView.as_view()),
    path("course/<str:slug>/faqs/", FAQView.as_view()),
    path("course/<str:slug>/faqs/<int:pk>/", FAQView.as_view()),
    path("course/<str:slug>/batches/", BatchView.as_view()),
    path("course/<str:slug>/batches/<int:pk>/", BatchView.as_view()),
    path("course/<str:slug>/blogs/", BlogView.as_view()),
    path("course/<str:slug>/blogs/<int:pk>/", BlogView.as_view()),
    path("course/<str:slug>/trainers/", TrainerView.as_view()),
    path("course/<str:slug>/trainers/<int:pk>/", TrainerView.as_view()),
]