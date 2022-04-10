from django.urls import path, re_path, include
from apps.add_object import views as add_views


urlpatterns = [
    path(r'^$', add_views.add_object, name='add_object'),
]
# не договор а контракт? бренд перед подрядчиком
# адрес, контакты, кто инжинер, законченный, 