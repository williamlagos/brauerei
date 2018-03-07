from django.contrib.auth.models import User, Group
from rest_framework import serializers
from brew.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'groups')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class ProfileSerializer(serializers.ModelSerializer):
    # user = serializers.HyperlinkedRelatedField(
    #     view_name='user-detail',
    #     read_only=True
    # )
    user = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Profile
        fields = ('user', 'lat', 'lon', 'name', 'description', 'address', 'photo', 'phone', 'side', 'rank')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'sku', 'name', 'description', 'photo')

class StockSerializer(serializers.HyperlinkedModelSerializer):
    key = ProductSerializer(many=False, read_only=True)
    provider = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=False, read_only=False)
    class Meta:
        model = Stock
        fields = ('key', 'provider', 'value', 'quantity')

class RequestSerializer(serializers.HyperlinkedModelSerializer):
    client = ProfileSerializer(read_only=True)
    provider = ProfileSerializer(read_only=True)
    products = ProductSerializer(many=True, read_only=True)
    client_id = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all(), many=False, write_only=True)
    provider_id = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all(), many=False, write_only=True)
    request_products = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True, write_only=True)
    class Meta:
        model = Request
        fields = ('id', 'client_id', 'provider_id', 'request_products', 'client', 'provider', 'products', 'estimated')
        depth = 1
    def create(self,validated_data):
        products = validated_data.pop('request_products')
        validated_data['provider'] = validated_data.pop('provider_id')
        validated_data['client'] = validated_data.pop('client_id')
        request = Request.objects.create(**validated_data)
        request.save()
        for p in products:
            s = Stock.objects.get(provider=validated_data['provider'],key=p)
            s.quantity -= 1
            s.save()
            request.products.add(p)
        return request
