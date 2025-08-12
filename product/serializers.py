from rest_framework import serializers
from .models import Product, Category, Review
from rest_framework.exceptions import ValidationError

class CategoryListSealizer(serializers.ModelSerializer):
    products_count = serializers.IntegerField(read_only=True)
    class Meta:
        model= Category
        fields = ['id', 'name', 'products_count']

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
        fields = 'id text product stars'.split()

class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class ProductReviewSerializer(serializers.ModelSerializer):
    reviews = ReviewListSealizer(many = True)
    rating = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ['id', 'title', 'reviews', 'category', 'rating']
    
    def get_rating(self, obj):
         reviews = obj.reviews.all()
         if not reviews:
             return None
         return round(sum(i.stars for i in reviews)/len(reviews),2)


class ProductValidationSerializer(serializers.Serializer):
    description = serializers.CharField(max_length=256)
    price = serializers.IntegerField()
    category_id = serializers.IntegerField
    rating = serializers.IntegerField(default=0)


class CategoryValidationSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 256)

class ReviewValidationSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=256)
    product_id = serializers.IntegerField()
    stars = serializers.IntegerField(default=5)