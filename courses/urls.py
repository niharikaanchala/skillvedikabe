from django.urls import path
from .views import (
    CourseListView,
    CourseDetailView,
    CourseBulkDeleteView,
    CourseByCategoryView,
    CoursesHeroView,
    CoursesWhyLearnView,
    CoursesCTAView,
    CoursesFAQView,
    CoursesPageContentView,  # ✅ import the new combined view
    CourseCounsellingSubmitView,
    CourseCounsellingListView,
    CourseCounsellingDetailView,
)

urlpatterns = [
    # Courses CRUD
    path('', CourseListView.as_view()),
    path('<int:id>/', CourseDetailView.as_view()),
    path('delete-multiple/', CourseBulkDeleteView.as_view()),
    path('category/<int:category_id>/', CourseByCategoryView.as_view()),

    # Courses Page Sections
    path('hero/', CoursesHeroView.as_view()),
    path('why-learn/', CoursesWhyLearnView.as_view()),
    path('cta/', CoursesCTAView.as_view()),
    path('faq/', CoursesFAQView.as_view()),

    # 🔥 Combined endpoint for all sections
    path('courses-page-content/', CoursesPageContentView.as_view()),  # ✅ Add this
    path("counselling/submit/", CourseCounsellingSubmitView.as_view()),
    path("counselling/", CourseCounsellingListView.as_view()),
    path("counselling/<int:pk>/", CourseCounsellingDetailView.as_view()),
]