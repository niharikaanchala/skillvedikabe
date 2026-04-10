from django.urls import path
from .views import *

urlpatterns = [

    # FULL PAGE
    path("contact-page/", ContactPageAPI.as_view()),

    # HERO
    path("hero/", ContactHeroAPI.as_view()),
    path("hero/<int:pk>/", ContactHeroDetailAPI.as_view()),

    # CONTACT INFO
    path("info/", ContactInfoAPI.as_view()),
    path("info/<int:pk>/", ContactInfoDetailAPI.as_view()),
    path("info/bulk-create/", ContactInfoBulkCreateAPI.as_view()),
    path("info/bulk-delete/", ContactInfoBulkDeleteAPI.as_view()),

    # DEMO
    path("demo/", DemoAPI.as_view()),
    path("demo/<int:pk>/", DemoDetailAPI.as_view()),

    # FORM
    path("form/", ContactFormAPI.as_view()),
    path("form/<int:pk>/", ContactFormDetailAPI.as_view()),

    # META TAGS
    path("meta-tags/", MetaTagsAPI.as_view()),
    path("meta-tags/<int:pk>/", MetaTagsDetailAPI.as_view()),
    path("meta-tags/bulk-delete/", MetaTagsBulkDeleteAPI.as_view()),
    path("meta-tags/delete/", MetaTagsDeleteAPI.as_view()),
]