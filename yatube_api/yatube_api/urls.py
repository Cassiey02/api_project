from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
]
