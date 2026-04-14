from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView

from backend.admin_auth import AdminObtainTokenView

urlpatterns = [
    path('api/course-details/', include('course_details.urls')),
    path("api/token/", AdminObtainTokenView.as_view(), name="admin_token_obtain"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="admin_token_refresh"),
    path('api/categories/', include('categories.urls')),
    path('api/courses/', include('courses.urls')),
    path('api/blog/', include('blog.urls')),
    path('api/home/', include('home.urls')),
    path('api/career/', include('career.urls')),
    path('api/on-job-support/', include('on_job_support.urls')),
    path('api/corporate-training/', include('corporate_training.urls')),
    path('api/about/', include('about.urls')),
    path('api/instructor/', include('instructor.urls')),
    path('api/contact/', include('contact.urls')),
    path('api/settings_app/', include('settings_app.urls')),
    path('api/legal/', include('legal_pages.urls')),

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)