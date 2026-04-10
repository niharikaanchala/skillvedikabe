from django.urls import path
from .views import (
    CorporateTrainingContentAPIView,
    HeroAPIView,
    EmpowerAPIView,
    PortfolioAPIView,
    AdvantageAPIView,
    ProcessAPIView,
    DemoAPIView,
    MetaTagsAPI,
    MetaTagsDetailAPI,
    SectionContentAPI,
)

urlpatterns = [
    path('', CorporateTrainingContentAPIView.as_view(), name='corporate-training-content'),

    # META TAGS (SEO)
    path('meta-tags/', MetaTagsAPI.as_view(), name='corporate-training-meta-tags'),
    path('meta-tags/<int:pk>/', MetaTagsDetailAPI.as_view(), name='corporate-training-meta-tags-detail'),
    path('section-content/', SectionContentAPI.as_view(), name='corporate-training-section-content'),

    # HERO
    path('hero/', HeroAPIView.as_view(), name='hero-list'),          # GET all, POST
    path('hero/<int:pk>/', HeroAPIView.as_view(), name='hero-detail'), # GET, PUT, PATCH, DELETE

    # EMPOWER
    path('empower/', EmpowerAPIView.as_view(), name='empower-list'),
    path('empower/<int:pk>/', EmpowerAPIView.as_view(), name='empower-detail'),

    # PORTFOLIO
    path('portfolio/', PortfolioAPIView.as_view(), name='portfolio-list'),
    path('portfolio/<int:pk>/', PortfolioAPIView.as_view(), name='portfolio-detail'),

    # ADVANTAGE
    path('advantage/', AdvantageAPIView.as_view(), name='advantage-list'),
    path('advantage/<int:pk>/', AdvantageAPIView.as_view(), name='advantage-detail'),

    # PROCESS
    path('process/', ProcessAPIView.as_view(), name='process-list'),
    path('process/<int:pk>/', ProcessAPIView.as_view(), name='process-detail'),

    # DEMO FORM
    path('demo/', DemoAPIView.as_view(), name='demo-list'),
    path('demo/<int:pk>/', DemoAPIView.as_view(), name='demo-detail'),
]