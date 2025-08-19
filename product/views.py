from rest_framework import generics, status
from rest_framework.response import Response
from django.db.models import Count

from .models import Category, Product, Review
from .serializers import (
    CategoryListSealizer,
    CategoryDetailSerializer,
    ProductListSealizer,
    ProductDetailSerializer,
    ReviewDetailSerializer,
    ReviewListSealizer,
    ProductReviewSerializer,
    ProductValidationSerializer,
    CategoryValidationSerializer,
    ReviewValidationSerializer
)


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.annotate(products_count=Count('products'))
    serializer_class = CategoryListSealizer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = CategoryListSealizer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = CategoryValidationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        category = Category.objects.create(name=serializer.validated_data['name'])
        return Response(CategoryDetailSerializer(category).data, status=status.HTTP_201_CREATED)


class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    lookup_field = "id"

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CategoryValidationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance.name = serializer.validated_data["name"]
        instance.save()
        return Response(CategoryDetailSerializer(instance).data, status=status.HTTP_201_CREATED)


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSealizer

    def create(self, request, *args, **kwargs):
        serializer = ProductValidationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = Product.objects.create(**serializer.validated_data)
        return Response(ProductDetailSerializer(product).data, status=status.HTTP_201_CREATED)


class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = "id"

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ProductValidationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        for attr, value in serializer.validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return Response(ProductDetailSerializer(instance).data, status=status.HTTP_201_CREATED)


class ReviewListCreateAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewListSealizer

    def create(self, request, *args, **kwargs):
        serializer = ReviewValidationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        review = Review.objects.create(**serializer.validated_data)
        return Response(ReviewDetailSerializer(review).data, status=status.HTTP_201_CREATED)


class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewDetailSerializer
    lookup_field = "id"

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ReviewValidationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        for attr, value in serializer.validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return Response(ReviewDetailSerializer(instance).data, status=status.HTTP_201_CREATED)


class ProductReviewAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductReviewSerializer
