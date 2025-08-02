from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CategoryListSealizer, CategoryDetailSerializer , ProductListSealizer, ProductDetailSerializer, ReviewDetailSerializer, ReviewListSealizer
from .models import Category , Product, Review
# Create your views here.



@api_view(['GET'])
def category_detail_api_view(request, id):
    try:
        category = Category.objects.get(id = id)
    except Category.DoesNotExist:
        return Response(data = {'error': 'Category not found!'},
                        status=status.HTTP_404_NOT_FOUND
                        )
    data = CategoryDetailSerializer(category).data
    return Response(data = data)


@api_view(['GET'])
def category_list_api_view(request):
    category = Category.objects.all()

    data = CategoryListSealizer(category, many = True).data

    return Response(
            data = data,
            status = status.HTTP_200_OK
        )


@api_view(['GET'])
def product_list_api_view(request):
    product = Product.objects.all()

    data = ProductListSealizer(product, many = True).data

    return Response(
            data = data,
            status = status.HTTP_200_OK
        )


@api_view(['GET'])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id = id)
    except Product.DoesNotExist:
        return Response(data = {'error': 'Product not found!'},
                        status=status.HTTP_404_NOT_FOUND
                        )
    data = ProductDetailSerializer(product).data
    return Response(data = data)


@api_view(['GET'])
def review_list_api_view(request):
    review = Review.objects.all()

    data = ReviewListSealizer(review, many = True).data

    return Response(
            data = data,
            status = status.HTTP_200_OK
        )


@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id = id)
    except Review.DoesNotExist:
        return Response(data = {'error': 'Review not found!'},
                        status=status.HTTP_404_NOT_FOUND
                        )
    data = ReviewDetailSerializer(review).data
    return Response(data = data)