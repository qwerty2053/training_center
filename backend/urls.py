from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from student.views import StudentViewSet
from course.views import CourseViewSet
from score.views import ScoreViewSet


router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'scores', ScoreViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/students/<int:pk>/enroll/<int:course_id>/', StudentViewSet.as_view({'post': 'enroll'}),
         name='student-enroll'),
]

if settings.DEBUG:

    from drf_spectacular.views import (SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView)

    urlpatterns += [
        path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
        path("swagger/", SpectacularSwaggerView.as_view(url_name="api-schema"), name="api-docs"),
        path('redoc/', SpectacularRedocView.as_view(url_name='api-schema'), name='redoc'),
    ]
