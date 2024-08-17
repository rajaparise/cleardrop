"""proj_main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Pricing API",
        default_version='v1',
        url='https://localhost:8000',
        license=openapi.License(name="Swagger License", url='https://swagger.io/license/'),
    ),
    public=True,
)

from proj_main import views

urlpatterns = [
    path('cd/admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('cd/tests/', include('cleardrop.urls')),
    path('cd/', views.TestViewSet.as_view({'get': 'list'}), name = 'test'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('__debug__/', include(debug_toolbar.urls)),
]

urlpatterns += staticfiles_urlpatterns()
