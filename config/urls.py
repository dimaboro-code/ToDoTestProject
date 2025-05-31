from django.contrib import admin
from django.urls import path, include
from tasks.urls import urlpatterns as task_urls
from users.urls import urlpatterns as user_urls
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="ToDo API",
        default_version='v1',
        description="Документация к ToDo API",
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include(user_urls)),
    path('', include(task_urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
