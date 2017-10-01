from django.conf.urls import url, include
from engine.api import *
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="empty.html")),
    url(r'^products$', ProductResource.as_list()),
    url(r'^products/(?P<pk>\d+)$', ProductResource.as_detail()),
    url(r'^stocks$', StockResource.as_list()),
    url(r'^stocks/(?P<pk>\d+)$', StockResource.as_detail()),
    url(r'^requests$', RequestResource.as_list()),
    url(r'^requests/(?P<pk>\d+)$', RequestResource.as_detail()),
    url(r'^providers$', ProviderResource.as_list()),
    url(r'^providers/(?P<pk>\d+)$', ProviderResource.as_detail()),
    url(r'^clients$', ClientResource.as_list()),
    url(r'^clients/(?P<pk>\d+)$', ClientResource.as_detail()),
]
