from django.urls import path
from swagger.views import schema_view
from . import views

urlpatterns = [
    path('', views.schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/personnel/', views.Personnel.as_view(), name='api-personnel'),
]
