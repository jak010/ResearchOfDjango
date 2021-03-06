"""config URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

# API 문서용
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

scheme_url_patters = [
    path("authenticate/", include('authenticate.urls'))

]

scheme_view_v1 = get_schema_view(
    openapi.Info(
        title="Open API",
        default_version="v1",
        description="Document API",
        terms_of_service="https://127.0.0.1:8000/"
    ),
    public=True,
    permission_classes=(AllowAny,),
    patterns=scheme_url_patters
)

urlpatterns = [
    #  API Document !
    url(r'^swagger(?P<format>\.json|\.yaml)$', scheme_view_v1.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', scheme_view_v1.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', scheme_view_v1.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # App URL
    path('admin/', admin.site.urls),
    path("authenticate/", include('authenticate.urls'))

]
