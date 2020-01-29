from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from .quickstart import views
from django.conf import settings
from django.conf.urls.static import static

# Create a router to direct to the various viewset endpoints.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'employees', views.EmployeeViewSet)
router.register(r'projects', views.ProjectViewSet)

# Wire up our API using automatic URL routing.
urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path(r'', views.IndexView.as_view(), name='index'),
    path(r'projects/', views.ProjectView.as_view(), name='projects'),
    path(r'employees/<employee>/', views.EmployeeView.as_view(), name="employee"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

