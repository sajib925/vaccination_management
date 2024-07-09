from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/bookings/", include("bookings.urls")),
    path("api/campaign/", include("campaign.urls")),
    path("api/review/", include("review.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("api/auth/", include("dj_rest_auth.urls")),
    path("api/auth/registration/",include("dj_rest_auth.registration.urls")),
    path("api/auth/", include("django.contrib.auth.urls")),
]
