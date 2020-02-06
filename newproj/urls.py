from django.contrib import admin
from django.urls import path,include
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls import url
schema_view = get_swagger_view(title='Deployment of service on cloud..!')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include('appone.emp_routes')),
    path('api/v2/', include('apptwo.prod_router')),
    url(r'^rapi/', include('rest_framework.urls')),
    url(r'^$', schema_view),
]
