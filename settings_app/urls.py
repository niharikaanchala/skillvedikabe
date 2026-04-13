from django.urls import path
from .views import (
    get_settings,
    get_setting,
    create_setting,
    update_setting,
    delete_setting,
)

urlpatterns = [
    path("", get_settings),              # GET all
    path("<int:pk>/", get_setting),      # GET one
    path("create/", create_setting),     # POST
    path("<int:pk>/update/", update_setting),  # PUT
    path("<int:pk>/delete/", delete_setting),   # DELETE
]