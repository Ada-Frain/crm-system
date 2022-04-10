from django.urls import path, re_path, include
from apps.core import views as core_views


urlpatterns = [
    path('', core_views.home_page, name='home'),
    re_path(r'^(?P<slug>[-\w]+)/$', core_views.project_detail, name='project_detail'),
    path('accounts/', include('django.contrib.auth.urls')),
]
