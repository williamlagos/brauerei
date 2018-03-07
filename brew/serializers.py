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
        fields = ('key', 'user', 'provider', 'value', 'quantity')

class RequestSerializer(serializers.HyperlinkedModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=False, read_only=False)
    provider = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=False, read_only=False)
    products = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True, read_only=False)
    class Meta:
        model = Request
        fields = ('id', 'client', 'provider', 'products', 'estimated')
