from restless.dj import DjangoResource
from engine.models import Product,Profile,User,Stock,Request

class ProductResource(DjangoResource):

    # GET /products
    def list(self):
        return Product.objects.all()

    # GET /products/deliveries/<pk>/
    def detail(self, pk, **kwargs):
        return Product.objects.get(id=pk)

    # POST /products
    def create(self):
        pass
