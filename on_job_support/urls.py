from django.urls import path
from .views import (
    HeroViewSet,
    RealTimeHelpViewSet,
    AudienceViewSet,
    HelpViewSet,
    StepViewSet,
    WhyChooseViewSet,
    DemoViewSet,
    DemoRequestViewSet,
    MetaTagsAPI,
    MetaTagsDetailAPI,
    SectionContentAPI,
)

# --- Hero ---
hero_list = HeroViewSet.as_view({'get': 'list', 'post': 'create'})
hero_detail = HeroViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})
hero_bulk_delete = HeroViewSet.as_view({'post': 'bulk_delete'})

# --- RealTimeHelp ---
realtime_list = RealTimeHelpViewSet.as_view({'get': 'list', 'post': 'create'})
realtime_detail = RealTimeHelpViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})
realtime_bulk_delete = RealTimeHelpViewSet.as_view({'post': 'bulk_delete'})

# --- Audience ---
audience_list = AudienceViewSet.as_view({'get': 'list', 'post': 'create'})
audience_detail = AudienceViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})
audience_bulk_delete = AudienceViewSet.as_view({'post': 'bulk_delete'})

# --- Help ---
help_list = HelpViewSet.as_view({'get': 'list', 'post': 'create'})
help_detail = HelpViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})
help_bulk_delete = HelpViewSet.as_view({'post': 'bulk_delete'})

# --- Steps ---
steps_list = StepViewSet.as_view({'get': 'list', 'post': 'create'})
steps_detail = StepViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})
steps_bulk_delete = StepViewSet.as_view({'post': 'bulk_delete'})

# --- WhyChoose ---
why_list = WhyChooseViewSet.as_view({'get': 'list', 'post': 'create'})
why_detail = WhyChooseViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})
why_bulk_delete = WhyChooseViewSet.as_view({'post': 'bulk_delete'})

# --- Demo ---
demo_list = DemoViewSet.as_view({'get': 'list', 'post': 'create'})
demo_detail = DemoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})
demo_bulk_delete = DemoViewSet.as_view({'post': 'bulk_delete'})

# --- DemoRequest ---
demo_request_list = DemoRequestViewSet.as_view({'get': 'list', 'post': 'create'})
demo_request_detail = DemoRequestViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})
demo_request_bulk_delete = DemoRequestViewSet.as_view({'post': 'bulk_delete'})

urlpatterns = [
    # Hero
    path('hero/', hero_list, name='hero-list'),
    path('hero/<int:pk>/', hero_detail, name='hero-detail'),
    path('hero/bulk-delete/', hero_bulk_delete, name='hero-bulk-delete'),

    # RealTimeHelp
    path('realtime-help/', realtime_list, name='realtime-list'),
    path('realtime-help/<int:pk>/', realtime_detail, name='realtime-detail'),
    path('realtime-help/bulk-delete/', realtime_bulk_delete, name='realtime-bulk-delete'),

    # Audience
    path('audience/', audience_list, name='audience-list'),
    path('audience/<int:pk>/', audience_detail, name='audience-detail'),
    path('audience/bulk-delete/', audience_bulk_delete, name='audience-bulk-delete'),

    # Help
    path('help/', help_list, name='help-list'),
    path('help/<int:pk>/', help_detail, name='help-detail'),
    path('help/bulk-delete/', help_bulk_delete, name='help-bulk-delete'),

    # Steps
    path('steps/', steps_list, name='steps-list'),
    path('steps/<int:pk>/', steps_detail, name='steps-detail'),
    path('steps/bulk-delete/', steps_bulk_delete, name='steps-bulk-delete'),

    # WhyChoose
    path('why-choose/', why_list, name='why-list'),
    path('why-choose/<int:pk>/', why_detail, name='why-detail'),
    path('why-choose/bulk-delete/', why_bulk_delete, name='why-bulk-delete'),

    # Demo
    path('demo/', demo_list, name='demo-list'),
    path('demo/<int:pk>/', demo_detail, name='demo-detail'),
    path('demo/bulk-delete/', demo_bulk_delete, name='demo-bulk-delete'),

    # DemoRequest
    path('demo-request/', demo_request_list, name='demo-request-list'),
    path('demo-request/<int:pk>/', demo_request_detail, name='demo-request-detail'),
    path('demo-request/bulk-delete/', demo_request_bulk_delete, name='demo-request-bulk-delete'),

    # MetaTags (SEO)
    path("meta-tags/", MetaTagsAPI.as_view(), name="on-job-support-meta-tags"),
    path("meta-tags/<int:pk>/", MetaTagsDetailAPI.as_view(), name="on-job-support-meta-tags-detail"),
    path("section-content/", SectionContentAPI.as_view(), name="on-job-support-section-content"),
]