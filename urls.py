from django.contrib import admin
from django.urls import path, include
from django.urls import path, include
from recruitment.views import home
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from tasks.views.task_viewset import TaskViewSet 
from django.core.wsgi import get_wsgi_application

# Django WSGI application
application = get_wsgi_application()

# Django Rest Framework Router
router = DefaultRouter()
router.register(r"tasks", TaskViewSet)

# Combined URL patterns
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),  # ✅ Add this line for root URL
    path("home/", home, name="home"),  # ✅ Add this line for `/home/`
    path("recruitment/", include("recruitment.urls")),  # ✅ Ensure recruitment URLs are included
    path("tasks/", include("tasks.urls")),  # ✅ Ensure tasks URLs are included
]

# Static files in DEBUG mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
