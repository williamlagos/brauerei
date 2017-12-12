# from restless.dj import DjangoResource
# from engine.models import Product,Profile,User,Stock,Request
#
# class ProductResource(DjangoResource):
#
#     # GET /products
#     def list(self):
#         return Product.objects.all()
#
#     # GET /products/<pk>/
#     def detail(self, pk, **kwargs):
#         return Product.objects.get(id=pk)
#
#     # POST /products
#     def create(self):
#         pass
#
# class StockResource(DjangoResource):
#
#     # GET /stocks
#     def list(self):
#         return Stock.objects.all()
#
#     # GET /stocks/<pk>/
#     def detail(self, pk, **kwargs):
#         return Stock.objects.get(id=pk)
#
#     # POST /stocks
#     def create(self):
#         pass
#
# class RequestResource(DjangoResource):
#
#     # GET /requests
#     def list(self):
#         return Request.objects.all()
#
#     # GET /requests/<pk>/
#     def detail(self, pk, **kwargs):
#         return Request.objects.get(id=pk)
#
#     # POST /requests
#     def create(self):
#         pass
#
# class ProviderResource(DjangoResource):
#
#     # GET /providers
#     def list(self):
#         return Profile.objects.filter(side=1)
#
#     # GET /providers/<pk>/
#     def detail(self, pk, **kwargs):
#         return Profile.objects.filter(side=1,id=pk)
#
#     # POST /providers
#     def create(self):
#         pass
#
# class ClientResource(DjangoResource):
#
#     # GET /clients
#     def list(self):
#         return Profile.objects.filter(side=0)
#
#     # GET /clients/<pk>/
#     def detail(self, pk, **kwargs):
#         return Profile.objects.filter(side=0,id=pk)
#
#     # POST /clients
#     def create(self):
#         pass
