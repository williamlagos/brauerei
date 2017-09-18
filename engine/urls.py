from django.conf.urls import url, include
from engine.api import ProductResource

urlpatterns = [
    url(r'^products$', ProductResource.as_list(), name="kombi_deliveries"),
    url(r'^products/(?P<pk>\d+)$', ProductResource.as_detail(), name="kombi_delivery"),
]
