from rest_framework import serializers
from .models import Product, Category, Review

class CategoryListSealizer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields = 'id name'.split()

class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ProductListSealizer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields = 'id title description price category'.split()

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class ReviewListSealizer(serializers.ModelSerializer):
    class Meta:
        model= Review
        fields = 'id text product'.split()

class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"